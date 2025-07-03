const request = require("request");
const cheerio = require("cheerio");
const iconv = require("iconv-lite");

const getNews = () => {
    request(
        {
            url: "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=103&sid2=241",
            method: "GET",
            encoding: null,
        },
        (error, response, body) => {
            if (error) {
                console.error(error);
                return;
            }
            if (response.statusCode === 200) {
                console.log("response ok");
                const bodyDecoded = iconv.decode(body, "euc-kr");
                const $ = cheerio.load(bodyDecoded);

                const list_text_inner_arr = $(
                    "#main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(even) > dl"
                ).toArray();

                var result = [];
                list_text_inner_arr.forEach((div) => {
                    const aLast = $(div).find("a").last();
                    const path = aLast.attr("href");
                    const url = `${path}`;
                    const title = aLast.text().trim();

                    result.push({
                        url,
                        title,
                    });
                });
                console.log(result);
            }
        }
    );
};

getNews();
