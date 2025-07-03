from flask import Blueprint, render_template, request
from db import get_db_connection, get_cursor

hospital_bp = Blueprint('hospital', __name__)

@hospital_bp.route('/hos.html')
def hos():
    return render_template('hos.html')

@hospital_bp.route('/hos_result', methods=['POST'])
def hos_result():
    name = request.form.get('name')
    area = request.form.get('area')
    sub = request.form.get('sub')
    conn = get_db_connection()
    cursor = get_cursor(conn)
    sql = "SELECT * FROM hos_table where hos_name like '%{}%' and hos_area like '%{}%' and hos_sub like '%{}%'".format(name,area,sub)
    cursor.execute(sql)
    data_list = cursor.fetchall()
    conn.close()
    return render_template('hos_result.html',data_list=data_list,name=name,area=area,sub=sub) 