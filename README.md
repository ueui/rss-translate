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
 - source005 [https://siftrss.com/f/WYvvrkAkgX](https://siftrss.com/f/WYvvrkAkgX) -> [特集_日経クロストレンド](rss/%E7%89%B9%E9%9B%86_%E6%97%A5%E7%B5%8C%E3%82%AF%E3%83%AD%E3%82%B9%E3%83%88%E3%83%AC%E3%83%B3%E3%83%89)
 - source006 [https://fetchrss.com/rss/620d11a970b7d1781324262266e2f73edf2f98627b0e7aa2.xml](https://fetchrss.com/rss/620d11a970b7d1781324262266e2f73edf2f98627b0e7aa2.xml) -> [Research_Commentary_Brookings](rss/Research_Commentary_Brookings)
 - source007 [http://fetchrss.com/rss/620d11a970b7d1781324262267d7ba1d141b09f2900edc32.xml](http://fetchrss.com/rss/620d11a970b7d1781324262267d7ba1d141b09f2900edc32.xml) -> [Commentary_and_Articles_RAND](rss/Commentary_and_Articles_RAND)
 - source008 [https://politepol.com/fd/gSkM6dQ8BdqG.xml](https://politepol.com/fd/gSkM6dQ8BdqG.xml) -> [Culture_The Economist](rss/Culture_The%20Economist)
 - source009 [https://kill-the-newsletter.com/feeds/kxnraollt2n0gd03szin.xml](https://kill-the-newsletter.com/feeds/kxnraollt2n0gd03szin.xml) -> [Carnegieendowment](rss/Carnegieendowment)
 - source010 [https://politepol.com/fd/LES08YuDyITn.xml](https://politepol.com/fd/LES08YuDyITn.xml) -> [Culture_GQ](rss/Culture_GQ)
 - source011 [https://politepol.com/fd/k2KTqKohLdMD.xml](https://politepol.com/fd/k2KTqKohLdMD.xml) -> [Pew_Research_Center](rss/Pew_Research_Center)
 - source012 [https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/spotlight/on-politics/rss.xml](https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/spotlight/on-politics/rss.xml) -> [NYT_U.S._Politics](rss/NYT_U.S._Politics)
 - source013 [https://politepol.com/fd/6UsKHJLrGfgp.xml](https://politepol.com/fd/6UsKHJLrGfgp.xml) -> [Briefing The Economist](rss/Briefing%20The%20Economist)
 - source014 [https://fetchrss.com/rss/6518f1be2d18ae56d5360f7265d35fc7c43c5356173e4013.xml](https://fetchrss.com/rss/6518f1be2d18ae56d5360f7265d35fc7c43c5356173e4013.xml) -> [Ideas_Morgan_Stanley](rss/Ideas_Morgan_Stanley)
 - source015 [http://rsshub.umzzz.com/reuters/legal/legalindustry](http://rsshub.umzzz.com/reuters/legal/legalindustry) -> [Legal_Industry_Law_Firm_News_Reuters](rss/Legal_Industry_Law_Firm_News_Reuters)
 - source016 [https://www.bloomberg.com/authors/ARbTQlRLRjE/matthew-s-levine.rss](https://www.bloomberg.com/authors/ARbTQlRLRjE/matthew-s-levine.rss) -> [Matt_Levine_Bloomberg_Opinion_Columnist](rss/Matt_Levine_Bloomberg_Opinion_Columnist)
 - source017 [http://fetchrss.com/rss/620d11a970b7d1781324262267d7bb44b787a0de3a0025c2.xml](http://fetchrss.com/rss/620d11a970b7d1781324262267d7bb44b787a0de3a0025c2.xml) -> [SpecialReportsfromReutersjournalistsaroundtheworld](rss/SpecialReportsfromReutersjournalistsaroundtheworld)
 - source018 [http://fetchrss.com/rss/5fd1017a86229a5e2b65bb5267d7be8f837b0b0b47087f32.xml](http://fetchrss.com/rss/5fd1017a86229a5e2b65bb5267d7be8f837b0b0b47087f32.xml) -> [Blerdy Otome A Dash of Black Girl Magic in Every Review](rss/Blerdy%20Otome%20A%20Dash%20of%20Black%20Girl%20Magic%20in%20Every%20Review)
 - source019 [https://forbes.com/sites/billhardekopf/feed](https://forbes.com/sites/billhardekopf/feed) -> [Bill_Hardekopf](rss/Bill_Hardekopf)
 - source020 [https://politepol.com/fd/C8JCiAISyeUs.xml](https://politepol.com/fd/C8JCiAISyeUs.xml) -> [Forbes_Daily](rss/Forbes_Daily)
 - source021 [https://fetchrss.com/rss/61c328520dbe482d810dbec2667c93bbba9f15b9a309f962.xml](https://fetchrss.com/rss/61c328520dbe482d810dbec2667c93bbba9f15b9a309f962.xml) -> [Goings_On_The_New_Yorker](rss/Goings_On_The_New_Yorker)
 - source022 [https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/series/us-morning-briefing/rss.xml](https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/series/us-morning-briefing/rss.xml) -> [NYT_The_Morning_Newsletter](rss/NYT_The_Morning_Newsletter)
 - source023 [https://perezhilton.com/category/controversy/feed](https://perezhilton.com/category/controversy/feed) -> [Controversy Archives - Perez Hilton](rss/Controversy%20Archives%20-%20Perez%20Hilton)
 - source024 [https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/books/review/rss.xml](https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/books/review/rss.xml) -> [Book_Review_The_New_York_Times](rss/Book_Review_The_New_York_Times)
 - source025 [https://politepol.com/fd/cvqP0wDPuxlB.xml](https://politepol.com/fd/cvqP0wDPuxlB.xml) -> [U.S.Environmental_ProtectionAgency_Perspectives](rss/U.S.Environmental_ProtectionAgency_Perspectives)
 - source026 [http://fetchrss.com/rss/5fd1017a86229a5e2b65bb5267d7bed2297e1745eb088902.xml](http://fetchrss.com/rss/5fd1017a86229a5e2b65bb5267d7bed2297e1745eb088902.xml) -> [Henley_&_Partners_Press_Media_Articles](rss/Henley_%26_Partners_Press_Media_Articles)
 - source027 [https://politepol.com/fd/A4Zkx42Ty32F.xml](https://politepol.com/fd/A4Zkx42Ty32F.xml) -> [Henley_&_Partners_Press_Releases](rss/Henley_%26_Partners_Press_Releases)
 - source028 [https://politepol.com/fd/NNLIg5PEAJ5L.xml](https://politepol.com/fd/NNLIg5PEAJ5L.xml) -> [Science technology The Economist](rss/Science%20technology%20The%20Economist)
 - source029 [https://perezhilton.com/category/love-line/feed](https://perezhilton.com/category/love-line/feed) -> [Love Line Archives - Perez Hilton](rss/Love%20Line%20Archives%20-%20Perez%20Hilton)
 - source030 [http://fetchrss.com/rss/67d7a50657856d2fd2016ed267d7c7ad9c7f1b1e5605a852.xml](http://fetchrss.com/rss/67d7a50657856d2fd2016ed267d7c7ad9c7f1b1e5605a852.xml) -> [Celebrity Legal & Lawsuits](rss/Celebrity%20Legal%20%26%20Lawsuits)
 - source031 [https://politepol.com/fd/DX6BTsW4AqS0.xml](https://politepol.com/fd/DX6BTsW4AqS0.xml) -> [Harvard Law Review](rss/Harvard%20Law%20Review)
 - source032 [https://www.pipes.digital/feed/K9P4A79D?](https://www.pipes.digital/feed/K9P4A79D?) -> [事件の最新ニュース記事一覧_週刊女性PRIME](rss/%E4%BA%8B%E4%BB%B6%E3%81%AE%E6%9C%80%E6%96%B0%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7_%E9%80%B1%E5%88%8A%E5%A5%B3%E6%80%A7PRIME)
 - source033 [https://www.pipes.digital/feed/LOM87bNr?](https://www.pipes.digital/feed/LOM87bNr?) -> [炎上の最新ニュース記事一覧_週刊女性PRIME](rss/%E7%82%8E%E4%B8%8A%E3%81%AE%E6%9C%80%E6%96%B0%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7_%E9%80%B1%E5%88%8A%E5%A5%B3%E6%80%A7PRIME)
 - source034 [http://fetchrss.com/rss/620d11a970b7d1781324262267d7bcbd75a2d5e8770a9792.xml](http://fetchrss.com/rss/620d11a970b7d1781324262267d7bcbd75a2d5e8770a9792.xml) -> [騒動事件の記事ニュース速報_ORICON_NEWS](rss/%E9%A8%92%E5%8B%95%E4%BA%8B%E4%BB%B6%E3%81%AE%E8%A8%98%E4%BA%8B%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E9%80%9F%E5%A0%B1_ORICON_NEWS)
 - source035 [http://fetchrss.com/rss/620d11a970b7d1781324262267d7bcfc1c4ee1882b0d8943.xml](http://fetchrss.com/rss/620d11a970b7d1781324262267d7bcfc1c4ee1882b0d8943.xml) -> [活動進退の記事ニュース速報_ORICON_NEWS](rss/%E6%B4%BB%E5%8B%95%E9%80%B2%E9%80%80%E3%81%AE%E8%A8%98%E4%BA%8B%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E9%80%9F%E5%A0%B1_ORICON_NEWS)
 - source036 [http://fetchrss.com/rss/63305985bee5754dab6c2ae267d7c1bbe36da311d808cdb3.xml](http://fetchrss.com/rss/63305985bee5754dab6c2ae267d7c1bbe36da311d808cdb3.xml) -> [週刊文春_編集部_プロフィール_文春オンライン](rss/%E9%80%B1%E5%88%8A%E6%96%87%E6%98%A5_%E7%B7%A8%E9%9B%86%E9%83%A8_%E3%83%97%E3%83%AD%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB_%E6%96%87%E6%98%A5%E3%82%AA%E3%83%B3%E3%83%A9%E3%82%A4%E3%83%B3)
 - source037 [http://fetchrss.com/rss/61c328520dbe482d810dbec267d7c1225734b0a49b069a32.xml](http://fetchrss.com/rss/61c328520dbe482d810dbec267d7c1225734b0a49b069a32.xml) -> [メディア掲載情報_ニホンモニター株式会社](rss/%E3%83%A1%E3%83%87%E3%82%A3%E3%82%A2%E6%8E%B2%E8%BC%89%E6%83%85%E5%A0%B1_%E3%83%8B%E3%83%9B%E3%83%B3%E3%83%A2%E3%83%8B%E3%82%BF%E3%83%BC%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BE)
 - source038 [http://fetchrss.com/rss/67d7a50657856d2fd2016ed267d7c28d0f7d55cff30db702.xml](http://fetchrss.com/rss/67d7a50657856d2fd2016ed267d7c28d0f7d55cff30db702.xml) -> [SNS発ニュース_ORICON_NEWS](rss/SNS%E7%99%BA%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9_ORICON_NEWS)
 - source039 [http://fetchrss.com/rss/67d7a50657856d2fd2016ed267d7c2b5837b0b0b47087f34.xml](http://fetchrss.com/rss/67d7a50657856d2fd2016ed267d7c2b5837b0b0b47087f34.xml) -> [マンガ特集_ORICON_NEWS](rss/%E3%83%9E%E3%83%B3%E3%82%AC%E7%89%B9%E9%9B%86_ORICON_NEWS)
 - source040 [http://fetchrss.com/rss/67d7a50657856d2fd2016ed267d824a7dffb2fb8b6075d63.xml](http://fetchrss.com/rss/67d7a50657856d2fd2016ed267d824a7dffb2fb8b6075d63.xml) -> [US Supreme Court](rss/US%20Supreme%20Court)
 - source041 [https://www.nature.com/nature.rss](https://www.nature.com/nature.rss) -> [NATURE BRIEFING](rss/NATURE%20BRIEFING)
 - source042 [https://news.google.com/search?q=ママ活&hl=ja&gl=JP&ceid=JP:ja](https://news.google.com/search?q=ママ活&hl=ja&gl=JP&ceid=JP:ja) -> [Google_ニュース検索_ママ活](rss/Google_%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E6%A4%9C%E7%B4%A2_%E3%83%9E%E3%83%9E%E6%B4%BB)
 - source043 [http://fetchrss.com/rss/6091364872635734406c61f267ea8e8a478137c6c108af72.xml](http://fetchrss.com/rss/6091364872635734406c61f267ea8e8a478137c6c108af72.xml) -> [パパ活_検索結果_日刊SPA!](rss/%E3%83%91%E3%83%91%E6%B4%BB_%E6%A4%9C%E7%B4%A2%E7%B5%90%E6%9E%9C_%E6%97%A5%E5%88%8ASPA%21)
