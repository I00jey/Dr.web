from flask import Blueprint, render_template, request
from db import get_db_connection, get_cursor

emergency_bp = Blueprint('emergency', __name__)

@emergency_bp.route('/emer.html')
def emer():
    return render_template('emer.html')

@emergency_bp.route('/emer_result', methods=['POST'])
def emer_result():
    name = request.form.get('name')
    area = request.form.get('area')
    conn = get_db_connection()
    cursor = get_cursor(conn)
    sql = "SELECT * FROM emergency where emer_name like '%{}%' and emer_area like '%{}%'".format(name,area)
    cursor.execute(sql)
    data_list = cursor.fetchall()
    conn.close()
    return render_template('emer_result.html',data_list=data_list,name=name,area=area) 