from flask import Blueprint, render_template, request
from db import get_db_connection, get_cursor

board_bp = Blueprint("board", __name__)


def get_board_cursor():
    conn = get_db_connection()
    cursor = get_cursor(conn)
    return conn, cursor


@board_bp.route("/gae.html")
def gae():
    conn, cursor = get_board_cursor()
    sql = "SELECT * from board"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    data_list = list(reversed(data_list))
    conn.close()
    return render_template("gae.html", data_list=data_list)


@board_bp.route("/gae_view", methods=["POST"])
def gae_view():
    gaeviewnum = request.form.get("gaeviewnum")
    conn, cursor = get_board_cursor()
    sql = "SELECT * FROM board where num = '{}'".format(gaeviewnum)
    sql_re = "SELECT * FROM reply where board_num = '{}'".format(gaeviewnum)
    cursor.execute(sql)
    data_list_board = cursor.fetchall()
    cursor.execute(sql_re)
    data_list_reply = cursor.fetchall()
    len_reply = len(data_list_reply)
    post_num = data_list_board[0][0] if data_list_board else None
    conn.commit()
    conn.close()
    return render_template(
        "gae_view.html",
        data_list_board=data_list_board,
        data_list_reply=data_list_reply,
        len_reply=len_reply,
        post_num=post_num,
    )


@board_bp.route("/gae_write.html")
def write():
    return render_template("gae_write.html")


@board_bp.route("/gae_write", methods=["POST"])
def gae_write():
    title = request.form.get("title")
    writer = request.form.get("writer")
    content = request.form.get("content")
    conn, cursor = get_board_cursor()
    sql = "INSERT INTO board (title, writer, content, write_date) VALUES ( %s, %s, %s,date(now()))"
    values = (title, writer, content)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    return gae()


@board_bp.route("/reply_write", methods=["POST"])
def reply_write():
    writer = request.form.get("re_writer")
    content = request.form.get("re_content")
    gaeviewnum = request.form.get("gaeviewnum")
    print(f"gaeviewnum: {gaeviewnum}")
    conn, cursor = get_board_cursor()
    sql = "INSERT INTO reply (re_writer,re_content,board_num) VALUES ( %s, %s, %s)"
    values = (writer, content, gaeviewnum)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    return gae()


@board_bp.route("/gong.html")
def gong():
    conn, cursor = get_board_cursor()
    sql = "SELECT * from gong_board"
    sql1 = "SELECT * from gong2"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    cursor.execute(sql1)
    gong_list = cursor.fetchall()
    data_list = reversed(data_list)
    conn.close()
    return render_template("gong.html", data_list=data_list, gong_list=gong_list)


@board_bp.route("/gong_view", methods=["POST"])
def gong_view():
    viewnum = request.form.get("viewnum")
    conn, cursor = get_board_cursor()
    sql = "SELECT * FROM gong_board where num = '{}'".format(viewnum)
    cursor.execute(sql)
    data_list_view = cursor.fetchall()
    conn.commit()
    conn.close()
    return render_template("gong_view.html", data_list=data_list_view)


@board_bp.route("/gong_view1", methods=["POST"])
def gong_view1():
    gong_number = request.form.get("gong_number")
    conn, cursor = get_board_cursor()
    sql = "SELECT * FROM gong2 where num = '{}'".format(gong_number)
    cursor.execute(sql)
    data_list_view = cursor.fetchall()
    conn.commit()
    conn.close()
    return render_template("gong_view1.html", gong_list=data_list_view)
