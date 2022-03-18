# Class: GeographicExposure
_A geographic exposure is a factor relating to geographic proximity to some impactful entity._





URI: [biolink:GeographicExposure](https://w3id.org/biolink/vocab/GeographicExposure)




## Inheritance

* [EnvironmentalExposure](EnvironmentalExposure.md) [ exposure event]
    * **GeographicExposure** [ exposure event]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [timepoint](timepoint.md) | [time_type](time_type.md) | 0..1 | a point in time  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: geographic exposure
close_mappings:
- dcid:GeologicalEvent
narrow_mappings:
- dcid:IceStoremEvent
- dcid:LakeEffectSnowEvent
- dcid:LandslideEvent
- dcid:MarineDenseFogEvent
- dcid:MarineLighteningEvent
- dcid:MarineStrongWindEvent
- dcid:MarineThunderstormWindEvent
- dcid:StormEvent
- dcid:StormSurgeTideEvent
- dcid:StrongWindEvent
- dcid:ThunderstormWindEvent
- dcid:TornadoEvent
- dcid:TropicalDepressionEvent
- dcid:WinterStoremEvent
description: A geographic exposure is a factor relating to geographic proximity to
  some impactful entity.
from_schema: https://w3id.org/biolink/biolink-model
is_a: environmental exposure
mixins:
- exposure event

```
</details>

### Induced

<details>
```yaml
name: geographic exposure
close_mappings:
- dcid:GeologicalEvent
narrow_mappings:
- dcid:IceStoremEvent
- dcid:LakeEffectSnowEvent
- dcid:LandslideEvent
- dcid:MarineDenseFogEvent
- dcid:MarineLighteningEvent
- dcid:MarineStrongWindEvent
- dcid:MarineThunderstormWindEvent
- dcid:StormEvent
- dcid:StormSurgeTideEvent
- dcid:StrongWindEvent
- dcid:ThunderstormWindEvent
- dcid:TornadoEvent
- dcid:TropicalDepressionEvent
- dcid:WinterStoremEvent
description: A geographic exposure is a factor relating to geographic proximity to
  some impactful entity.
from_schema: https://w3id.org/biolink/biolink-model
is_a: environmental exposure
mixins:
- exposure event
attributes:
  timepoint:
    name: timepoint
    description: a point in time
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    alias: timepoint
    owner: geographic exposure
    range: time type

```
</details>