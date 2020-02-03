# flask-basic
A basic demonstration on how to use a flask server backend.
The application gets a country name and displays the income level. The worldbank API is used, however, it has a limitation in which it takes ISO 3166-1 alpha-2 code as input query. As a result, the backend needs to convert the country name into ISO 3166-1 alpha-2 code. After this is done, the API request (done through the backend as well in this case) is executed. 

Singapore -> SG -> High income

![Preview](/image.png)

The CSS in this example is not a main focus.
Further, the code features explainations in the form of comments.
