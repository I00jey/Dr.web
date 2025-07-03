from flask import Blueprint, render_template, request, redirect
from db import get_db_connection, get_cursor
import requests
from bs4 import BeautifulSoup
import os

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def start():
    req = requests.get(os.getenv("NEWS_URL"), headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(req.text, "html.parser")
    myList = []
    href = []
    for i in soup.select(
        "#main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a"
    ):
        href.append(i.attrs["href"])
        myList.append(i.text)
    for i in soup.select(
        "#main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(2) > dl > dt:nth-child(2) > a"
    ):
        href.append(i.attrs["href"])
        myList.append(i.text)
    for i in soup.select(
        "#main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(6) > dl > dt:nth-child(2) > a"
    ):
        href.append(i.attrs["href"])
        myList.append(i.text)
    for i in soup.select(
        "#main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(4) > dl > dt:nth-child(2) > a"
    ):
        href.append(i.attrs["href"])
        myList.append(i.text)
    for i in soup.select(
        "#main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(5) > dl > dt:nth-child(2) > a"
    ):
        href.append(i.attrs["href"])
        myList.append(i.text)
    return render_template("main.html", list=myList, list1=href)


@main_bp.route("/main.html")
def main():
    return start()


@main_bp.route("/developer.html")
def developer():
    return render_template("developer.html")


@main_bp.route("/pagestory.html")
def pagestory():
    return render_template("pagestory.html")


@main_bp.route("/search.html")
def search():
    return render_template("search.html")


@main_bp.route("/medi.html")
def medi():
    return render_template("medi.html")


@main_bp.route("/medi_result", methods=["POST"])
def medi_result():
    name = request.form.get("name")
    part = request.form.get("part")
    shape = request.form.get("shape")
    kind = request.form.get("kind")
    conn = get_db_connection()
    cursor = get_cursor(conn)
    sql = "SELECT * FROM medi_table where medi_name like '%{}%' and medi_kind like '%{}%' and medi_shape like '%{}%' and medi_part like '%{}%'".format(
        name, kind, shape, part
    )
    cursor.execute(sql)
    data_list = cursor.fetchall()
    conn.close()
    return render_template(
        "medi_result.html",
        data_list_medi=data_list,
        name=name,
        part=part,
        shape=shape,
        kind=kind,
    )


@main_bp.route("/search_redirect")
def search_redirect():
    query = request.args.get("search", "")
    if query:
        return redirect(f"https://www.google.co.kr/search?q={query}")
    return redirect("/")
