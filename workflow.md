# Add new content to the SSK (May 2019)

## Add new scenarios to the SSK front-end

* Beta works with a test account (ask trainer for the credentials)
* With the teiMeta form available at http://ssk.huma-num.fr/#/new-scenario, **users** are able to push new scenarios and steps to the SSK github repository


* **Admin** :
  * The new files are pushed to the  *drafts/* folders.
  * An admin has to copy these files, after they are checked in quality, to the publication folders, *scenarios/* and *steps/*;
  * **Admin** commits the files copy;

## New standards

Form work just fine at http://ssk.huma-num.fr/#/add-standard

## New resource

The form is available at http://ssk.huma-num.fr/#/add-resource:
* Users have to paste the link of the resource in the text box, and click  "Get resource metadata".
* After a short moment, the scrapped metadata is displayed (JSON format).
* Users can check them and click to "submit resource to zotero".  
* On click appreas a message like *"Resource has been succefull add to SSK's Zotero library with itemKey: HBGFXSLQ"*
* Users have to copy the itemKey code (8 alphanumerical characters) in case they want to link the resource to a step.

**Admin** triggers SSK webhook on the last commmit (no need to ), with Postman.
* Find the payload of the last commit at https://github.com/ParthenosWP4/SSK/settings/hooks/96111354
* copy the payload
* paste it in the body of the POST request in Postman
