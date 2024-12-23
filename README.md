#  Rss-Translation

## 这是一个外文RSS翻译转换订阅页面 

[![circle_translate](https://github.com/ueui/rss-translate/actions/workflows/circle_translate.yml/badge.svg)](https://github.com/ueui/rss-translate/actions/workflows/circle_translate.yml) [![Deploy](https://github.com/ueui/rss-translate/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/ueui/rss-translate/actions/workflows/jekyll-gh-pages.yml)

 💡重构翻译文件配置、更新Action环境依赖，添加不同翻译机制,已修复特殊字符转译

 📢查看 [项目修改完善、已添加源及使用说明](https://github.com/ueui/rss-translate/tree/main/illustrate)

 📢查看[ 本页 ](https://ueui.github.io/rss-translate) 参考自[ rss-translate ](https://github.com/talengu/rss-translate)

## 已转换翻译源
 - source001 [https://politepol.com/fd/reoQ2EA9MDxJ.xml](https://politepol.com/fd/reoQ2EA9MDxJ.xml) -> [bloomberg_news](rss/bloomberg_news.xml)
 - source002 [https://feeds.bloomberg.com/Crypto/news.rss](https://feeds.bloomberg.com/Crypto/news.rss) -> [Bloomberg_Crypto](rss/Bloomberg_Crypto.xml)
 - source003 [https://www.vice.com/en/rss?locale=en_us](https://www.vice.com/en/rss?locale=en_us) -> [English_VICE](rss/English_VICE.xml)
 - source004 [https://kill-the-newsletter.com/feeds/h541vjjth6mkic38ik3f.xml](https://kill-the-newsletter.com/feeds/h541vjjth6mkic38ik3f.xml) -> [Bloomberg](rss/Bloomberg.xml)
 - source005 [https://kill-the-newsletter.com/feeds/bhi9909b0d1dbhqq7o7h.xml](https://kill-the-newsletter.com/feeds/bhi9909b0d1dbhqq7o7h.xml) -> [Reuters_newsletters](rss/Reuters_newsletters.xml)
 - source006 [https://fetchrss.com/rss/620d11a970b7d1781324262266e2f73edf2f98627b0e7aa2.xml](https://fetchrss.com/rss/620d11a970b7d1781324262266e2f73edf2f98627b0e7aa2.xml) -> [Research_Commentary_Brookings](rss/Research_Commentary_Brookings.xml)
 - source007 [https://fetchrss.com/rss/620d11a970b7d1781324262266e2f4c31634514d1d0e1a32.xml](https://fetchrss.com/rss/620d11a970b7d1781324262266e2f4c31634514d1d0e1a32.xml) -> [Commentary_and_Articles_RAND](rss/Commentary_and_Articles_RAND.xml)
 - source008 [https://fetchrss.com/rss/6437f470034816381c2bcb926690a7ec65440a4de80b0252.xml](https://fetchrss.com/rss/6437f470034816381c2bcb926690a7ec65440a4de80b0252.xml) -> [Culture_|_The Economist](rss/Culture_%7C_The%20Economist.xml)
 - source009 [https://kill-the-newsletter.com/feeds/kxnraollt2n0gd03szin.xml](https://kill-the-newsletter.com/feeds/kxnraollt2n0gd03szin.xml) -> [Carnegieendowment](rss/Carnegieendowment.xml)
 - source010 [https://politepol.com/fd/LES08YuDyITn.xml](https://politepol.com/fd/LES08YuDyITn.xml) -> [Culture_GQ](rss/Culture_GQ.xml)
 - source011 [https://www.pewresearch.org/feed/](https://www.pewresearch.org/feed/) -> [Pew_Research_Center](rss/Pew_Research_Center.xml)
 - source012 [https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/spotlight/on-politics/rss.xml](https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/spotlight/on-politics/rss.xml) -> [NYT_U.S._Politics](rss/NYT_U.S._Politics.xml)
 - source013 [https://kill-the-newsletter.com/feeds/88lhiotcswouh2kqelf0.xml](https://kill-the-newsletter.com/feeds/88lhiotcswouh2kqelf0.xml) -> [bloomberg_Business_of_Space](rss/bloomberg_Business_of_Space.xml)
 - source014 [https://fetchrss.com/rss/6518f1be2d18ae56d5360f7265d35fc7c43c5356173e4013.xml](https://fetchrss.com/rss/6518f1be2d18ae56d5360f7265d35fc7c43c5356173e4013.xml) -> [Ideas_Morgan_Stanley](rss/Ideas_Morgan_Stanley.xml)
 - source015 [https://fetchrss.com/rss/620d11a970b7d1781324262266e5485ed46ec68d5f06da32.xml](https://fetchrss.com/rss/620d11a970b7d1781324262266e5485ed46ec68d5f06da32.xml) -> [Supreme_Court_Of_The_United_States_Reuters](rss/Supreme_Court_Of_The_United_States_Reuters.xml)
 - source016 [https://politepol.com/fd/j1rpG2cevFgH.xml](https://politepol.com/fd/j1rpG2cevFgH.xml) -> [Matt_Levine_Bloomberg_Opinion_Columnist](rss/Matt_Levine_Bloomberg_Opinion_Columnist.xml)
 - source017 [https://fetchrss.com/rss/6091364872635734406c61f267284473651587d4af00f432.xml](https://fetchrss.com/rss/6091364872635734406c61f267284473651587d4af00f432.xml) -> [SpecialReportsfromReutersjournalistsaroundtheworld](rss/SpecialReportsfromReutersjournalistsaroundtheworld.xml)
 - source018 [https://fetchrss.com/rss/6437f470034816381c2bcb926690a52fba2238d47b0c1bf2.xml](https://fetchrss.com/rss/6437f470034816381c2bcb926690a52fba2238d47b0c1bf2.xml) -> [All_weekly_editions_|_The_Economist](rss/All_weekly_editions_%7C_The_Economist.xml)
 - source019 [https://forbes.com/sites/billhardekopf/feed](https://forbes.com/sites/billhardekopf/feed) -> [Bill_Hardekopf](rss/Bill_Hardekopf.xml)
 - source020 [https://politepol.com/fd/C8JCiAISyeUs.xml](https://politepol.com/fd/C8JCiAISyeUs.xml) -> [Forbes_Daily](rss/Forbes_Daily.xml)
 - source021 [https://fetchrss.com/rss/61c328520dbe482d810dbec2667c93bbba9f15b9a309f962.xml](https://fetchrss.com/rss/61c328520dbe482d810dbec2667c93bbba9f15b9a309f962.xml) -> [Goings_On_|_The_New_Yorker](rss/Goings_On_%7C_The_New_Yorker.xml)
 - source022 [https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/series/us-morning-briefing/rss.xml](https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/series/us-morning-briefing/rss.xml) -> [NYT_>_The_Morning_Newsletter](rss/NYT_%3E_The_Morning_Newsletter.xml)
 - source023 [https://politepol.com/fd/iZVG8rUDvbg9.xml](https://politepol.com/fd/iZVG8rUDvbg9.xml) -> [Morning_Briefing_Asia_Bloomberg](rss/Morning_Briefing_Asia_Bloomberg.xml)
 - source024 [https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/books/review/rss.xml](https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/books/review/rss.xml) -> [Book_Review_The_New_York_Times](rss/Book_Review_The_New_York_Times.xml)
 - source025 [https://politepol.com/fd/cvqP0wDPuxlB.xml](https://politepol.com/fd/cvqP0wDPuxlB.xml) -> [U.S.Environmental_ProtectionAgency_Perspectives](rss/U.S.Environmental_ProtectionAgency_Perspectives.xml)
 - source026 [http://fetchrss.com/rss/5fd1017a86229a5e2b65bb52673f2e875b2ee091ae0947c2.xml](http://fetchrss.com/rss/5fd1017a86229a5e2b65bb52673f2e875b2ee091ae0947c2.xml) -> [Henley_&_Partners_Press_Media_Articles](rss/Henley_%26_Partners_Press_Media_Articles.xml)
 - source027 [http://fetchrss.com/rss/5fd1017a86229a5e2b65bb52673f3f5ed80f9deefa0e5162.xml](http://fetchrss.com/rss/5fd1017a86229a5e2b65bb52673f3f5ed80f9deefa0e5162.xml) -> [Henley_&_Partners_Press_Releases](rss/Henley_%26_Partners_Press_Releases.xml)
 - source028 [https://siftrss.com/f/klPPkl0rRg](https://siftrss.com/f/klPPkl0rRg) -> [特集：日経クロストレンド](rss/%E7%89%B9%E9%9B%86%EF%BC%9A%E6%97%A5%E7%B5%8C%E3%82%AF%E3%83%AD%E3%82%B9%E3%83%88%E3%83%AC%E3%83%B3%E3%83%89.xml)
 - source029 [https://politepol.com/fd/4xQQiGU8EYLt.xml](https://politepol.com/fd/4xQQiGU8EYLt.xml) -> [people_celebrity_legal_lawsuits](rss/people_celebrity_legal_lawsuits.xml)
 - source030 [https://politepol.com/fd/NNLIg5PEAJ5L.xml](https://politepol.com/fd/NNLIg5PEAJ5L.xml) -> [Science & technology | The Economist](rss/Science%20%26%20technology%20%7C%20The%20Economist.xml)
 - source031 [https://politepol.com/fd/6UsKHJLrGfgp.xml](https://politepol.com/fd/6UsKHJLrGfgp.xml) -> [Briefing | The Economist](rss/Briefing%20%7C%20The%20Economist.xml)
 - source032 []() -> [](rss/.xml)
 - source033 []() -> [](rss/.xml)
 - source034 []() -> [](rss/.xml)
