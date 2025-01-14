# rss-translate

rss translate any to any

![](https://github.com/ueui/rss-translate/workflows/circle_translate/badge.svg)
![](https://github.com/ueui/rss-translate/workflows/Deploy/badge.svg)

you can edit [test.ini](https://github.com/ueui/rss-translate/edit/main/test.ini) to add orginal rss url. [help](https://github.com/ueui/rss/issues/2)

next find the translated link in [https://talengu.github.io/rss-translate/](https://talengu.github.io/rss-translate/)

## 20230814 update
- support proxy mode. you can set `action = "proxy"` in test.ini like [source010](https://github.com/ueui/rss-translate/blob/f6648c5262f4fa0926310dbe43fff820bf727ac7/test.ini#L67).
 Proxy mode does not translate the rss, and directly show the original rss.

## 20230702 update 
- use [main2.py](https://github.com/ueui/rss-translate/blob/main/main2.py) in [circle_translate.yml](https://github.com/ueui/rss-translate/blob/aeb61bc36eb1a22fd003677b5209291cf7cb4a87/.github/workflows/circle_translate.yml#L38)
- atom is bad now base on an atom paraser to find. NOW SUPPORT
        use [feedparser](https://pythonhosted.org/feedparser/)
- fix google translate limit . NOW SUPPORT

## rss translate links

 - source001 [https://politepol.com/fd/reoQ2EA9MDxJ.xml](https://politepol.com/fd/reoQ2EA9MDxJ.xml) -> [bloomberg_news](rss/bloomberg_news)
 - source002 [https://feeds.bloomberg.com/Crypto/news.rss](https://feeds.bloomberg.com/Crypto/news.rss) -> [Bloomberg_Crypto](rss/Bloomberg_Crypto)
 - source003 [https://www.vice.com/en/rss?locale=en_us](https://www.vice.com/en/rss?locale=en_us) -> [English_VICE](rss/English_VICE)
 - source004 [https://kill-the-newsletter.com/feeds/h541vjjth6mkic38ik3f.xml](https://kill-the-newsletter.com/feeds/h541vjjth6mkic38ik3f.xml) -> [Bloomberg](rss/Bloomberg)
 - source005 [https://siftrss.com/f/WYvvrkAkgX](https://siftrss.com/f/WYvvrkAkgX) -> [特集：日経クロストレンド](rss/%E7%89%B9%E9%9B%86%EF%BC%9A%E6%97%A5%E7%B5%8C%E3%82%AF%E3%83%AD%E3%82%B9%E3%83%88%E3%83%AC%E3%83%B3%E3%83%89)
 - source006 [https://fetchrss.com/rss/620d11a970b7d1781324262266e2f73edf2f98627b0e7aa2.xml](https://fetchrss.com/rss/620d11a970b7d1781324262266e2f73edf2f98627b0e7aa2.xml) -> [Research_Commentary_Brookings](rss/Research_Commentary_Brookings)
 - source007 [https://fetchrss.com/rss/620d11a970b7d1781324262266e2f4c31634514d1d0e1a32.xml](https://fetchrss.com/rss/620d11a970b7d1781324262266e2f4c31634514d1d0e1a32.xml) -> [Commentary_and_Articles_RAND](rss/Commentary_and_Articles_RAND)
 - source008 [https://fetchrss.com/rss/6437f470034816381c2bcb926690a7ec65440a4de80b0252.xml](https://fetchrss.com/rss/6437f470034816381c2bcb926690a7ec65440a4de80b0252.xml) -> [Culture_|_The Economist](rss/Culture_%7C_The%20Economist)
 - source009 [https://kill-the-newsletter.com/feeds/kxnraollt2n0gd03szin.xml](https://kill-the-newsletter.com/feeds/kxnraollt2n0gd03szin.xml) -> [Carnegieendowment](rss/Carnegieendowment)
 - source010 [https://politepol.com/fd/LES08YuDyITn.xml](https://politepol.com/fd/LES08YuDyITn.xml) -> [Culture_GQ](rss/Culture_GQ)
 - source011 [https://politepol.com/fd/k2KTqKohLdMD.xml](https://politepol.com/fd/k2KTqKohLdMD.xml) -> [Pew_Research_Center](rss/Pew_Research_Center)
 - source012 [https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/spotlight/on-politics/rss.xml](https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/spotlight/on-politics/rss.xml) -> [NYT_U.S._Politics](rss/NYT_U.S._Politics)
 - source013 [https://politepol.com/fd/6UsKHJLrGfgp.xml](https://politepol.com/fd/6UsKHJLrGfgp.xml) -> [Briefing | The Economist](rss/Briefing%20%7C%20The%20Economist)
 - source014 [https://fetchrss.com/rss/6518f1be2d18ae56d5360f7265d35fc7c43c5356173e4013.xml](https://fetchrss.com/rss/6518f1be2d18ae56d5360f7265d35fc7c43c5356173e4013.xml) -> [Ideas_Morgan_Stanley](rss/Ideas_Morgan_Stanley)
 - source015 [http://rsshub.umzzz.com/reuters/legal/legalindustry](http://rsshub.umzzz.com/reuters/legal/legalindustry) -> [Legal_Industry_Law_Firm_News_Reuters](rss/Legal_Industry_Law_Firm_News_Reuters)
 - source016 [https://www.bloomberg.com/authors/ARbTQlRLRjE/matthew-s-levine.rss](https://www.bloomberg.com/authors/ARbTQlRLRjE/matthew-s-levine.rss) -> [Matt_Levine_Bloomberg_Opinion_Columnist](rss/Matt_Levine_Bloomberg_Opinion_Columnist)
 - source017 [https://fetchrss.com/rss/6091364872635734406c61f267284473651587d4af00f432.xml](https://fetchrss.com/rss/6091364872635734406c61f267284473651587d4af00f432.xml) -> [SpecialReportsfromReutersjournalistsaroundtheworld](rss/SpecialReportsfromReutersjournalistsaroundtheworld)
 - source018 [https://politepol.com/fd/nI9kMzDM9k1y.xml](https://politepol.com/fd/nI9kMzDM9k1y.xml) -> [All_weekly_editions_|_The_Economist](rss/All_weekly_editions_%7C_The_Economist)
 - source019 [https://forbes.com/sites/billhardekopf/feed](https://forbes.com/sites/billhardekopf/feed) -> [Bill_Hardekopf](rss/Bill_Hardekopf)
 - source020 [https://politepol.com/fd/C8JCiAISyeUs.xml](https://politepol.com/fd/C8JCiAISyeUs.xml) -> [Forbes_Daily](rss/Forbes_Daily)
 - source021 [https://fetchrss.com/rss/61c328520dbe482d810dbec2667c93bbba9f15b9a309f962.xml](https://fetchrss.com/rss/61c328520dbe482d810dbec2667c93bbba9f15b9a309f962.xml) -> [Goings_On_|_The_New_Yorker](rss/Goings_On_%7C_The_New_Yorker)
 - source022 [https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/series/us-morning-briefing/rss.xml](https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/series/us-morning-briefing/rss.xml) -> [NYT_>_The_Morning_Newsletter](rss/NYT_%3E_The_Morning_Newsletter)
 - source023 [https://rssweball.top/feed/48df3ce3-d363-4154-8877-394273fbb43f.xml](https://rssweball.top/feed/48df3ce3-d363-4154-8877-394273fbb43f.xml) -> [Controversy Archives - Perez Hilton](rss/Controversy%20Archives%20-%20Perez%20Hilton)
 - source024 [https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/books/review/rss.xml](https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/books/review/rss.xml) -> [Book_Review_The_New_York_Times](rss/Book_Review_The_New_York_Times)
 - source025 [https://politepol.com/fd/cvqP0wDPuxlB.xml](https://politepol.com/fd/cvqP0wDPuxlB.xml) -> [U.S.Environmental_ProtectionAgency_Perspectives](rss/U.S.Environmental_ProtectionAgency_Perspectives)
 - source026 [http://fetchrss.com/rss/5fd1017a86229a5e2b65bb52673f2e875b2ee091ae0947c2.xml](http://fetchrss.com/rss/5fd1017a86229a5e2b65bb52673f2e875b2ee091ae0947c2.xml) -> [Henley_&_Partners_Press_Media_Articles](rss/Henley_%26_Partners_Press_Media_Articles)
 - source027 [http://fetchrss.com/rss/5fd1017a86229a5e2b65bb52673f3f5ed80f9deefa0e5162.xml](http://fetchrss.com/rss/5fd1017a86229a5e2b65bb52673f3f5ed80f9deefa0e5162.xml) -> [Henley_&_Partners_Press_Releases](rss/Henley_%26_Partners_Press_Releases)
 - source028 [https://politepol.com/fd/NNLIg5PEAJ5L.xml](https://politepol.com/fd/NNLIg5PEAJ5L.xml) -> [Science & technology | The Economist](rss/Science%20%26%20technology%20%7C%20The%20Economist)
 - source029 [https://rssweball.top/feed/78133558-58ab-487c-adb3-30069dba550a.xml](https://rssweball.top/feed/78133558-58ab-487c-adb3-30069dba550a.xml) -> [Love Line Archives - Perez Hilton](rss/Love%20Line%20Archives%20-%20Perez%20Hilton)
 - source030 [https://fetchrss.com/rss/620d11a970b7d178132426226774bd2f143c9ce271003ea2.xml](https://fetchrss.com/rss/620d11a970b7d178132426226774bd2f143c9ce271003ea2.xml) -> [Celebrity Legal & Lawsuits](rss/Celebrity%20Legal%20%26%20Lawsuits)
 - source031 [https://politepol.com/fd/DX6BTsW4AqS0.xml](https://politepol.com/fd/DX6BTsW4AqS0.xml) -> [Harvard Law Review](rss/Harvard%20Law%20Review)
 - source032 [http://fetchrss.com/rss/5fd1017a86229a5e2b65bb5267723449b1c81601a20136b2.xml](http://fetchrss.com/rss/5fd1017a86229a5e2b65bb5267723449b1c81601a20136b2.xml) -> [Blerdy Otome | A Dash of Black Girl Magic in Every Review](rss/Blerdy%20Otome%20%7C%20A%20Dash%20of%20Black%20Girl%20Magic%20in%20Every%20Review)
 - source033 [https://www.pipes.digital/feed/K9P4A79D?](https://www.pipes.digital/feed/K9P4A79D?) -> [事件の最新ニュース・記事一覧 | 週刊女性PRIME](rss/%E4%BA%8B%E4%BB%B6%E3%81%AE%E6%9C%80%E6%96%B0%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E3%83%BB%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7%20%7C%20%E9%80%B1%E5%88%8A%E5%A5%B3%E6%80%A7PRIME)
 - source034 [https://www.pipes.digital/feed/LOM87bNr?](https://www.pipes.digital/feed/LOM87bNr?) -> [炎上の最新ニュース・記事一覧 | 週刊女性PRIME](rss/%E7%82%8E%E4%B8%8A%E3%81%AE%E6%9C%80%E6%96%B0%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E3%83%BB%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7%20%7C%20%E9%80%B1%E5%88%8A%E5%A5%B3%E6%80%A7PRIME)
 - source035 [http://fetchrss.com/rss/620d11a970b7d17813242622678660e609b164a24d03f332.xml](http://fetchrss.com/rss/620d11a970b7d17813242622678660e609b164a24d03f332.xml) -> [炎上の最新ニュース・記事一覧 | 週刊女性PRIME](rss/%E7%82%8E%E4%B8%8A%E3%81%AE%E6%9C%80%E6%96%B0%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E3%83%BB%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7%20%7C%20%E9%80%B1%E5%88%8A%E5%A5%B3%E6%80%A7PRIME)
 - source036 [http://fetchrss.com/rss/620d11a970b7d17813242622678660d1f96a4c28fc000483.xml](http://fetchrss.com/rss/620d11a970b7d17813242622678660d1f96a4c28fc000483.xml) -> [事件の最新ニュース・記事一覧 | 週刊女性PRIME](rss/%E4%BA%8B%E4%BB%B6%E3%81%AE%E6%9C%80%E6%96%B0%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E3%83%BB%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7%20%7C%20%E9%80%B1%E5%88%8A%E5%A5%B3%E6%80%A7PRIME)
