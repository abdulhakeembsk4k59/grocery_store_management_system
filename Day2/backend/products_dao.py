import mysql.connector

def get_all_products():

    cnx = mysql.connector.connect(user='root', password='root',
                                host='127.0.0.1',
                                database='gs')

    cursor = cnx.cursor()
    query =  ("SELECT  products.product_id, products.product_name,"
    "products.uom_id, products.price_per_unit, uom.uom_name "
    "FROM products inner join uom on products.uom_id=uom.uom_id;")


    cursor.execute(query)

    response = []

    for(product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id' : product_id,
            'name': name,
            'uom_id':uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })

    cnx.close()
    return response
if __name__=='__main__':
    print(get_all_products())