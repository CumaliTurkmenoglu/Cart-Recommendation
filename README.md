# Cart Recommendation system Deployed as a REST API using Flask

* [Flask Restful Documentation]()
* [HTTPie Documentation](https://httpie.org/doc)
* [Data Source: HepsiBurada.com Data Scientist Assignment)

General file structure:

app.py: Flask API application
model.py: class object for classifier
requirements.txt: list of packages that the app will import
models folder: includes models, co-occurrence matrix, count and tf-idf vectorizers and
                       product_indexes for co-occurrence matrix
data folder: includes original data files


Start a virtual environment and install requirements from requirements.txt
Virtual Environment

1.  Go to app.py directory where `requirements.txt` is also located
2.  Create new virtual environment
	conda create --name py39 python=3.9.4
2. Activate virtual environment
source activate py39
3.4. Install required packages from `requirements.txt`
pip install -r requirements.txt

Testing the  cart recommendation API:

1. Go to directory with `app.py` and run the following command

“python app.py”

2. In a new terminal window, use HTTPie to make a GET request at the URL of the API.

“http http://127.0.0.1:5000/api/v1.0/recommendations/HBV00000AX6LR-HBV00000JUHBA”

The suffixes in the url are product ids in the cart and The system will recommend 10 items  for all items in the cart. For instance: If there are 2 items in the cart, 10/2=5 items will be recommended for each. If there are 3 items in the cart, 10/3=3.3..~=3 items will be recommended for each. 


An Expected json output

HTTP/1.0 200 OK
Content-Length: 3704
Content-Type: text/html; charset=utf-8
Date: Mon, 16 Aug 2021 10:26:41 GMT
Server: Werkzeug/2.0.1 Python/3.9.4

{
    "data": [
        {
            "brand": "Palette",
            "category": "Kişisel Bakım",
            "cooccurence": 2.0,
            "index": 0,
            "item_id_recommended_for": "HBV00000AX6LR",
            "item_name_recommended_for": " palet kalmak doğal renk papatya",
            "name": " palet kalmak doğal renk sahra sarı",
            "productid": "HBV00000AX6LT",
            "subcategory": "Saç Bakımı"
        },
        {
            "brand": "Palette",
            "category": "Kişisel Bakım",
            "cooccurence": 2.0,
            "index": 1,
            "item_id_recommended_for": "HBV00000AX6LR",
            "item_name_recommended_for": " palet kalmak doğal renk papatya",
            "name": " palet kalmak doğal renk siyah",
            "productid": "HBV00000AX6LV",
            "subcategory": "Saç Bakımı"
        },
        {
            "brand": "Boron",
            "category": "Ev Bakım ve Temizlik",
            "cooccurence": 2.0,
            "index": 2,
            "item_id_recommended_for": "HBV00000AX6LR",
            "item_name_recommended_for": " palet kalmak doğal renk papatya",
            "name": " boro doğal mineral temiz ürün doğal renk renk yıkamak",
            "productid": "HBV00000P7W3K",
            "subcategory": "Çamaşır Yıkama"
        },
        {
            "brand": "Palette",
            "category": "Kişisel Bakım",
            "cooccurence": 2.0,
            "index": 3,
            "item_id_recommended_for": "HBV00000AX6LR",
            "item_name_recommended_for": " palet kalmak doğal renk papatya",
            "name": " palet kalmak doğal renk ko kumral",
            "productid": "HBV00000AX6LL",
            "subcategory": "Saç Bakımı"
        },
        {
            "brand": "Palette",
            "category": "Kişisel Bakım",
            "cooccurence": 2.0,
            "index": 4,
            "item_id_recommended_for": "HBV00000AX6LR",
            "item_name_recommended_for": " palet kalmak doğal renk papatya",
            "name": " palet kalmak doğal renk bronz kahve",
            "productid": "HBV00000AX6L9",
            "subcategory": "Saç Bakımı"
        },
        {
            "brand": "Tarım Kredi",
            "category": "Temel Gıda",
            "cooccurence": 10.0,
            "index": 5,
            "item_id_recommended_for": "HBV00000JUHBA",
            "item_name_recommended_for": " türkiye tar kredi koopyeşil mercimek",
            "name": " türkiye tar kredi koop kırmızı mercimek",
            "productid": "HBV00000JUHBC",
            "subcategory": "Bakliyat, Pirinç, Makarna"
        },
        {
            "brand": "Tarım Kredi",
            "category": "Temel Gıda",
            "cooccurence": 7.0,
            "index": 6,
            "item_id_recommended_for": "HBV00000JUHBA",
            "item_name_recommended_for": " türkiye tar kredi koopyeşil mercimek",
            "name": " tar kredi birlik osmancık pirinç",
            "productid": "HBV00000IFZG2",
            "subcategory": "Bakliyat, Pirinç, Makarna"
        },
        {
            "brand": "Tarım Kredi",
            "category": "Temel Gıda",
            "cooccurence": 6.0,
            "index": 7,
            "item_id_recommended_for": "HBV00000JUHBA",
            "item_name_recommended_for": " türkiye tar kredi koopyeşil mercimek",
            "name": " tar kredi birlik kuru fasulye",
            "productid": "HBV00000NFMNF",
            "subcategory": "Bakliyat, Pirinç, Makarna"
        },
        {
            "brand": "Carrefour",
            "category": "Temel Gıda",
            "cooccurence": 5.0,
            "index": 8,
            "item_id_recommended_for": "HBV00000JUHBA",
            "item_name_recommended_for": " türkiye tar kredi koopyeşil mercimek",
            "name": " carrefour yeşil mercimek",
            "productid": "HBV00000NE24H",
            "subcategory": "Bakliyat, Pirinç, Makarna"
        },
        {
            "brand": "Tarım Kredi",
            "category": "Temel Gıda",
            "cooccurence": 5.0,
            "index": 9,
            "item_id_recommended_for": "HBV00000JUHBA",
            "item_name_recommended_for": " türkiye tar kredi koopyeşil mercimek",
            "name": " türkiye tar kredi koop nohut",
            "productid": "HBV00000JUHB6",
            "subcategory": "Bakliyat, Pirinç, Makarna"
        }
    ],
    "schema": {
        "fields": [
            {
                "name": "index",
                "type": "integer"
            },
            {
                "name": "productid",
                "type": "string"
            },
            {
                "name": "brand",
                "type": "string"
            },
            {
                "name": "category",
                "type": "string"
            },
            {
                "name": "subcategory",
                "type": "string"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "name": "cooccurence",
                "type": "number"
            },
            {
                "name": "item_name_recommended_for",
                "type": "string"
            },
            {
                "name": "item_id_recommended_for",
                "type": "string"
            }
        ],
        "pandas_version": "0.20.0",
        "primaryKey": [
            "index"
        ]
    }
}



