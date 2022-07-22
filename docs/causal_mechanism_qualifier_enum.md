---
grand_parent: Browse Biolink Model
parent: Enums
title: biolink:causal_mechanism_qualifier_enum
layout: default
---

# Class: causal_mechanism_qualifier_enum




URI: [biolink:causal_mechanism_qualifier_enum](https://w3id.org/biolink/vocab/causal_mechanism_qualifier_enum)


## Other properties

|  |  |  |
| --- | --- | --- |

## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| binding | A causal mechanism mediated by the direct contact between effector and target chemical or  biomolecular entity, which form a stable physical interaction. |  |  |
| inhibition | A causal mechanism in which the effector binds to the target and negatively effects its normal function,  e.g. prevention of enzymatic reaction or activation of downstream pathway. |  | {'is_a': 'binding'} |
| antibody inhibition | A causal mechanism in which an antibody specifically binds to and interferes with the target. |  | {'is_a': 'inhibition'} |
| antagonism | A causal mecahnism in which the effector binds to a receptor and prevents activation by an agonist  through competing for the binding site. |  | {'is_a': 'inhibition'} |
| molecular channel blockage | A causal mechanism in which the effector binds to a molecular channel and prevents or reduces  transport of ions through it. |  | {'is_a': 'inhibition'} |
| inverse agonism | A causal mechanism in which the effector binds to the same receptor-binding site as an agonist and antagonizes its effects, often exerting the opposite effect of the agonist by suppressing spontaneous receptor signaling. |  | {'is_a': 'inhibition'} |
| negative allosteric modulation | A causal mechanism in which the effector reduces or prevents the action of the endogenous ligand of a  receptor by binding to a site distinct from that ligand (i.e. non-competitive inhibition) |  | {'is_a': 'inhibition'} |
| agonism | A causal mechanism in which the effector binds and activates a receptor to mimic the effect of an  endogenous ligand. |  | {'is_a': 'activation'} |
| molecular channel opening | A causal mechanism in which the effector binds to a molecular channel and facilitates transport of  ions through it. |  | {'is_a': 'activation'} |
| positive allosteric modulation | A causal mechanism in which the effector enhances the action of the endogenous ligand of a receptor by  binding to a site distinct from that ligand (i.e. non-competitive inhibition) |  | {'is_a': 'activation'} |
| potentiation | A causal mechanism in which the effector  binds to and enhances or intensifies the effect of some  other chemical or drug on its target. |  | {'is_a': 'binding'} |
| activation | A causal mechanism in which the effector binds to and positively affects the normal functioning of its target. |  | {'is_a': 'binding'} |
| inducer | A causal mechanism in which the effector binds to and increases the activity/rate of an enzyme that  processes drugs in the body. |  | {'is_a': 'binding'} |
| transcriptional regulation | A causal mechanism mediated by through the control of target gene transcription |  |  |
| signaling-mediated control | A causal mechanism mediated by the activation or control of signaling events that influence the some aspect  of the target entity (e.g. its activity, processing, transport, etc) |  |  |

