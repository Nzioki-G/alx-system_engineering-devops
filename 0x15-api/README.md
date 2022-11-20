# API
**A**pplication **P**rogram **I**nterface: mechanism for application components to communicate
<br><br>
### REST API
**RE**presentational **S**tate **T**ransfer: an API that uses HTTP for communication
<br><br>
### Microservices
As I understand: **microservices** are modularisation on the client's side or runtime<br>
An application is modular. These modules have endpoints that listen and respond to each other<br>
Example
- objects of a program are microservices i.e. they each handle a specific problem<br>
- communication between objects is made possible by APIs i.e. the objects' public methods and properties

<br><br>
**REST API requests are made up of**
1. <span style="color: blue"> **endpoint** </span> - the url
2. <span style="color: blue"> **method** </span> - CRUD will be POST, GET, PUT, DELETE
3. <span style="color: blue"> **data** </span> - if method is POST/PUT
4. <span style="color: blue"> **headers** </span> - metadata e.g. content type
