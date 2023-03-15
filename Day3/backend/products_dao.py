from sql_connection import get_sql_connection


def get_all_products(connection):


    cursor = connection.cursor()

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
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into products" 
             "(product_name, uom_id, price_per_unit)"
             "values(%s, %s, %s);")
    
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid


if __name__=='__main__':
    connection = get_sql_connection()
    print(insert_new_product(connection, {
        'product_name': 'cabage',
        'uom_id':'1',
        'price_per_unit': '10'
    }))
