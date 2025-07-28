from flask import Blueprint, render_template, request, redirect
from db import get_db_connection, get_cursor
import requests
from bs4 import BeautifulSoup
import os

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def start():
    req = requests.get(os.getenv("NEWS_URL"), headers={"User-Agent": "Mozilla/5.0"})
    print("응답 상태코드 ->", req.status_code)
    # print("응답 내용일부", req.text[:500])
    soup = BeautifulSoup(req.text, "html.parser")
    newsList = []
    href = []
    newsImg = []

    # #newsct > div.section_latest > div > div.section_latest_article._CONTENT_LIST._PERSIST_META > div:nth-child(1) > ul > li:nth-child(1) > div > div > div.sa_thumb._LAZY_LOADING_ERROR_HIDE > div > a > img
    articles = soup.select(
        "#newsct > div.section_latest > div > div.section_latest_article._CONTENT_LIST._PERSIST_META > div:nth-child(1) > ul > li"
    )

    for article in articles:
        # 텍스트/링크 추출
        a_tag = article.select_one("div.sa_text > a")
        if a_tag:
            href.append(a_tag.get("href"))
            newsList.append(a_tag.get_text(strip=True))
        else:
            href.append(None)
            newsList.append("제목 없음")

        # 이미지 추출 (지연 로딩용 data-src 속성 사용)
        img_tag = article.select_one("div.sa_thumb img")
        if img_tag:
            img_url = img_tag.get("data-src")
            newsImg.append(img_url)
        else:
            newsImg.append(None)

    print(newsList)
    print(newsImg)
    print(href)
    return render_template("main.html", newsList=newsList, href=href, newsImg=newsImg)


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
