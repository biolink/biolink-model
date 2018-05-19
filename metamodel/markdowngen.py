"""Generate markdown

"""

import logging

from .manager import *
from .generator import Generator
from .yumlgen import YumlGenerator


    
class MarkdownGenerator(Generator):
        
    def serialize(self, dirname=None, **args):
        self.dirname = dirname
        self.tr()
    
    def tr(self):
        schema = self.schema
        dirname = self.dirname
        mgr = self.manager
        ixfile = '{}/index.md'.format(dirname)
        self.open_fh(ixfile)
        self.emit_header(2, schema.name)
        self.para(schema.description)
        roots = [c for c in schema.classes if not c.is_a]

        self.emit_anchor('classes')
        self.emit_header(3, 'Classes')
        for c in roots:
            if not mgr.classdef(c).mixin:
                self.write_class_hier(c)
        self.nl()
        
        self.emit_anchor('mixins')
        self.emit_header(3, 'Mixins')
        for c in roots:
            if mgr.classdef(c).mixin:
                self.write_class_hier(c)
        self.nl()

        self.emit_anchor('slots')
        self.emit_header(3, 'Predicates and Properties')
        for p in mgr.root_predicates():
            self.write_pred_hier(p)
            
                
        self.close_fh()

        for c in schema.classes:
            fn = self.class_dir_path(c)
            self.open_fh(fn)
            self.tr_class(c)
            self.close_fh()
        for s in schema.slots:
            fn = self.slot_dir_path(s)
            self.open_fh(fn)
            self.tr_slot(s)
            self.close_fh()
        
            
    def write_class_hier(self, c, level=0):
        mgr = self.manager
        self.bullet(self.link(c), level)
        for n in mgr.child_nodes(c):
            self.write_class_hier(n, level+1)
        
    def write_pred_hier(self, p, level=0):
        mgr = self.manager
        self.bullet(self.link(p), level)
        for n in mgr.child_nodes(p):
            self.write_pred_hier(n, level+1)
        
            
    def class_dir_path(self, c):
        cn = self.manager.class_name(c)
        return '{}/{}.md'.format(self.dirname, cn)
    
    def slot_dir_path(self, s):
        sn = self.manager.slot_name(s)
        return '{}/{}.md'.format(self.dirname, sn)

    def obj_name(self, obj):
        if isinstance(obj, str):
            # assume class...
            return self.cname(obj)
        if isinstance(obj, ClassDefinition):
            return self.cname(obj)
        else:
            return self.slot_name(obj)
    
    def cname(self, c):
        if isinstance(c,str):
            cn = c
        else:
            cn = self.manager.class_name(c)
        return cn

    def slot_name(self, s):
        return self.manager.slot_name(s)

    def tr_mappings(self, obj):
        schema = self.schema
        mgr = self.manager
        self.emit_header(2, 'Mappings')
        if obj.mappings:
            for m in obj.mappings:
                self.bullet(self.xlink(m))
        if isinstance(obj, ClassDefinition) and obj.subclass_of:
            self.bullet(self.xlink(obj.subclass_of))
        self.nl()
        
    def tr_slot(self, s):
        schema = self.schema
        mgr = self.manager

        s = mgr.slotdef(s)
        
        # header
        self.emit_header(2, s.name)

        self.para(s.description)

        uri = mgr.obj_uri(s)
        self.w('URI: [{}]({})\n'.format(uri, uri))

        self.tr_mappings(s)
        
        self.emit_header(2, 'Domain and Range')
        domain_cls = mgr.classdef(s.domain)
        range_cls = mgr.classdef(s.range)
        self.w('{} -> {}\n'.format(self.link(domain_cls), self.link(range_cls)))
        self.nl()
        
        self.emit_header(2, 'Inheritance')
        parent = s.is_a
        if parent is not None:
            self.bullet(' is_a: {}'.format(self.link(mgr.slotdef(parent))))
        self.nl()
            
        self.emit_header(2, 'Children')
        for n in mgr.child_nodes(s):
            self.bullet(' child: {}'.format(self.link(mgr.slotdef(n))))
        self.nl()

        self.emit_header(2, 'Used in')
        for c in schema.classes:
            for cs in mgr.class_slotdefs(c, True, True):
                if cs == s.name:
                    self.bullet(' usage: {}'.format(self.link(c)))
                if cs == 'relation':
                    ## HARDCODED BIOLINK ASSUMPTION
                    ## in biolink, associations are reified, and the 'relation'
                    ## slot of a reified association class will point to a specific relation
                    rc = mgr.class_slot_getattr(c, 'relation', 'subproperty_of', None)
                    if rc is not None and rc == s.name:
                        self.bullet(' usage: {}'.format(self.link(c)))                        
                    
            
    
    def tr_class(self, c):
        schema = self.schema
        mgr = self.manager

        c = mgr.classdef(c)
        
        # header
        cn = mgr.class_name(c)
        self.emit_header(2, c.name)

        self.para(c.description)

        uri = mgr.obj_uri(c)
        self.w('URI: [{}]({})\n'.format(uri, uri))

        yg = YumlGenerator(schema=schema)
        yg.tr_class(c, recurse=True)
        self.w('\n\n![img]({})'.format(yg.url()))
        self.nl()
        
        self.tr_mappings(c)
        
        self.emit_header(2, 'Inheritance')
        parent = c.is_a
        if parent is not None:
            self.bullet(' is_a: {}'.format(self.link(mgr.classdef(parent))))
        if c.mixins:
            for m in c.mixins:
                self.bullet(' mixin: {}'.format(self.link(mgr.classdef(m))))                
        self.nl()

        # show all child nodes except mixins
        self.emit_header(2, 'Children')
        for n in mgr.child_nodes(c, mixin=False):
            self.bullet(' child: {}'.format(self.link(mgr.classdef(n))))
        for n in mgr.child_nodes_by_mixin(c):
            self.bullet(' mixin: {}'.format(self.link(mgr.classdef(n))))
        self.nl()

        ucs = mgr.all_class_usages(c)
        if len(ucs) > 0:
            self.emit_header(2, 'Used in')
            for (uc,rc) in ucs:
                self.bullet(' class: {} references: {}'.format(self.link(mgr.classdef(uc)), self.link(mgr.classdef(rc))))
        
        self.nl()
                    
        self.emit_header(2, 'Fields')
        slots = mgr.class_slotdefs(c, True, True)
        for s in slots:
            s = mgr.slotdef(s, c)
            sn = self.slot_name(s)

            r = mgr.class_slot_range(c, s)
            if r:
                if mgr.classdef(r):
                    r = self.link(mgr.classdef(r))
                elif mgr.slotdef(r):
                    # reified relation
                    r = self.link(mgr.slotdef(r))

            qual = ''
            if mgr.class_slot_multivalued(c, s):
                qual = '*'
            if mgr.class_slot_getattr(c, s, 'required', False):
                qual = ' [required]'


            descr = mgr.class_slot_getattr(c, s, 'description', None)
            self.bullet("{}".format(self.link(s)))
            if descr:
                self.bullet("_{}_".format(descr), level=1)
            self.bullet("__range__: {}{}".format(r, qual), level=1)
            subproperty_of = mgr.class_slot_getattr(c, s, 'subproperty_of', None)
            if subproperty_of:
                relation = mgr.slotdef(subproperty_of)
                self.bullet('edge label: {}'.format(self.link(relation)), level=1)
            for ex in mgr.class_slot_getattr(c, s, 'examples', []):
                self.bullet('Example: {} {}'.format(self.xlink(ex.value), ex.description), level=1)
            defining_cls = mgr.class_slotdef_inherited_from(c, s)
            if defining_cls:
                if defining_cls.name == c.name:
                    self.bullet('__Local__', level=1)
                else:
                    self.bullet('inherited from: {}'.format(self.link(defining_cls)), level=1)


                
    ## --
    ## FORMATTING
    ## --

    def open_fh(self, fn):
        self.file = open(fn, 'w')
        self.frontmatter()
        
    def close_fh(self):
        self.file.close()
        self.file = None
        
    def w(self, txt, ftuple=() ):
        self.file.write(txt.format(*ftuple))

    def emit_anchor(self, id):
        self.w('<a name="{}"/>\n'.format(id))
        
    def emit_header(self, level, txt):
        self.w('{} {}\n\n', ('#' * level, txt))
                             
    def para(self, txt):
        self.w('\n{}\n\n'.format(txt))
                             
    def bullet(self, txt, level=0):
        self.w('{} * {}\n'.format('   ' * level, txt))

    def nl(self):
        self.w('\n')
        
    def frontmatter(self, layout='default'):
        self.w('---\nlayout: {}\n---\n\n'.format(layout))
                             
    def link(self, obj):
        if obj is None:
            return ''
        fn = self.obj_name(obj)
        s =  '[{}]({}.html)'.format(obj.name, fn)
        if obj.in_subset:
            s += " *subsets: " + " | ".join(obj.in_subset)+"*"
        return s
                             
    def xlink(self, id):
        url = self.id_to_url(id)
        return '[{}]({})'.format(id, url)
