
# The Standardization Survival Kit
## Hands-on Workshop

These pages contain the resources needed to take workshops about the [Standardization Survival Kit](http://ssk.huma-num.fr).

## Purpose of the workshop

1. Stress the importance of documenting research best practices;
1. Document them with the Standardization Survival Kit.

## The SSK in 5 minutes

### Concept
The Standardization Survival Kit (SSK) is a tool that supports the digital evolution within Social Sciences and Humanities research, by giving access to standards and best practices in a meaningful way, with the mediation of research scenarios. A research scenario is a (digital) workflow practiced by researchers, that can be repeatedly applied to a task that will help to gain material or insights in view of a research question.

These scenarios are at the core of the SSK, as they embed resources with contextual information and relevant examples on standardized processes and methods in a research context. The SSK is an open tool where users are able to publish new scenarios or adapt existing ones. These scenarios can be seen as a living memory of what should be the best research practices in a given community, made accessible and reusable for other researchers.

### SSK's survival kit
* Website: http://ssk.huma-num.fr
* Source: https://github.com/ParthenosWP4/SSK
* Documentation: https://ssk.readthedocs.io
* Bibliography:
  * Charles Riondet, Dorian Seillier, Lionel Tadjou, Laurent Romary. Standardization Survival Kit (Final). [Technical Report] Inria Paris. 2018. [〈hal-01925144〉](https://hal.inria.fr/hal-01925144)
  * Marie Puren, Charles Riondet, Laurent Romary, Dorian Seillier, Lionel Tadjou. SSK by example. Make your Arts and Humanities research go standard. Digital Humanities 2018 : "Bridges/Puentes", Jun 2018, Mexico, Mexico. https://dh2018.adho.org/en/. [〈hal-01848882〉](https://hal.inria.fr/hal-01848882)
  * Marie Puren, Charles Riondet, Laurent Romary, Dorian Seillier, Lionel Tadjou. The Standardization Survival Kit (SSK): Bringing best practices to research communities in the Humanities. Digital Humanities Benelux 2018, Jun 2018, Amsterdam, Netherlands. https://dhbenelux.socialhistoryservices.org/. [〈hal-01850075〉](https://hal.inria.fr/hal-01850075)


## Create a scenario

### Scenario writing guidelines

A tutorial with formal guidelines for creating a scenario can be found in the [SSK documentation](https://ssk.readthedocs.io/en/latest/1_tuto.html).

### Work with the TEI

Scenarios and steps are encoded with the standard [XML-TEI](http://tei-c.org/). All the information displayed within the SSK proceed from TEI files, hosted on the GitHub repository:
* scenarios: https://github.com/ParthenosWP4/SSK/tree/master/scenarios
* steps: https://github.com/ParthenosWP4/SSK/tree/master/steps

The documentation of the TEI data model can be found [here](https://ssk.readthedocs.io/en/latest/2_ssktei.html).

Users willing to create scenarios in TEI should follow the following
instructions:

-  Download or fork the SSK data repository in GitHub. It is necessary to have an account on GitHub: https://github.com/ParthenosWP4/SSK/tree/master/ (NB: to fork a repository, a GitHub user account is necessary);
-  Create TEI files with your favourite XML editor. Don't forget to validate them against the SSK schema;
-  To publish scenarios on the SSK, the TEI files need to be in the *scenarios* and *steps* folders;
-  Users with a GitHub account can make a pull request to ask for the update of the repository. Users without an account can contact the SSK team at ssk [at] inria [dot] fr.


### Add resources to the SSK Zotero Library

There is different ways to link resources to a step. The one we favour is the recording of the resource metadata in the dedicated SSK Zotero Library: https://www.zotero.org/groups/427927/ssk-parthenos/

1. To populate it, a Zotero account is necessary (create it  [here](https://www.zotero.org/user/register)) as well as a membership in the SSK group (apply [here](https://www.zotero.org/groups/427927/ssk-parthenos)).
![zot1](img/zot2.jpg) The SSK library is organized in collections and sub-collections, by domains or standards. To learn more about how to use Zotero, many tutorial and learning resources are available [here](https://www.zotero.org/support/screencast_tutorials).
![zot1](img/zot1.jpg)
1. Each group of resources (general and project specific) should be gathered. In the TEI, these groups are represented by `<linkGrp>` elements:
  1. One `<linkGrp>` for the general resources;
  1. one `<linkGrp>` for each project.
1. The references added to the Zotero Library are linked to the step with the help of their Zotero key, i.e. the last part of the URL of the resource record on the Zotero website. For instance, in the following example, the key is `4B62GJ5I`: *https://www.zotero.org/groups/427927/ssk-parthenos/items/itemKey/4B62GJ5I*. In TEI, the Zotero key should be used like this:
```xml
<ref type="zotero" key="4B62GJ5I"/ >
```
4. It is possible to put directly the URL of a Github repository or a document stored in HAL, and skip the Zotero part (the metadata would be fetched directly via the APIs)
