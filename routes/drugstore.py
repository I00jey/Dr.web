from flask import Blueprint, render_template, request
from db import get_db_connection, get_cursor

drugstore_bp = Blueprint('drugstore', __name__)

@drugstore_bp.route('/drugstore.html')
def drugstore():
    return render_template('drugstore.html')

@drugstore_bp.route('/drugstore_result', methods=['POST'])
def drugstore_result():
    name = request.form.get('name')
    area = request.form.get('area')
    conn = get_db_connection()
    cursor = get_cursor(conn)
    sql = "SELECT * FROM drugstore where drug_name like '%{}%' and drug_area like '%{}%'".format(name,area)
    cursor.execute(sql)
    data_list = cursor.fetchall()
    conn.close()
    return render_template('drugstore_result.html',data_list=data_list,name=name,area=area) 