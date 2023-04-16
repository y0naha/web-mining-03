import scrapy

class PromocoesJogosSpider(scrapy.Spider):
    name = "promocoes-jogos"
    allowed_domains = ["nuuvem.com"]

    start_urls = []
    url_base = "https://www.nuuvem.com/br-pt/catalog/sort/bestselling/sort-mode/desc/"
    num_pages = 10
    for i in range(1,num_pages+1,1):
        start_urls.append(f"{url_base}/page/{i}")

    def parse(self, response):
        for jogo in response.css(".product-card--grid"): 
            moeda = jogo.css(".product-card--grid .currency-symbol::text").get()
            inteiro = jogo.css(".product-card--grid .integer::text").get()
            decimal = jogo.css(".product-card--grid .decimal::text").get()
            sistema = [] 
            plataforma = []

            if  jogo.css(".product-card--grid .icon-steam").get() != None:
                sistema.append("steam")

            if  jogo.css(".product-card--grid .icon-windows").get() != None:
                sistema.append("windows")

            if  jogo.css(".product-card--grid .icon-linux").get() != None:
                sistema.append("linux")

            if  jogo.css(".product-card--grid .icon-mac").get() != None:
                sistema.append("mac")

            if  jogo.css(".product-card--grid .icon-nintendoswitch").get() != None:
                sistema.append("nintendo switch")

            if  jogo.css(".product-card--grid .icon-xboxone").get() != None:
                sistema.append("xbox one")

            if  jogo.css(".product-card--grid .icon-xboxseriessx").get() != None:
                sistema.append("xbox series s x")

            if  jogo.css(".product-card--grid .icon-ios").get() != None:
                sistema.append("ios")

            if  jogo.css(".product-card--grid .icon-android").get() != None:
                sistema.append("android")

            if  jogo.css(".product-card--grid .icon-nintendoswitch").get() != None:
                plataforma.append("nintendo")

            if  jogo.css(".product-card--grid .icon-microsoft").get() != None:
                plataforma.append("xbox")

            if  jogo.css(".product-card--grid .icon-playstationstore").get() != None:
                plataforma.append("playstation")

            if  jogo.css(".product-card--grid .icon-android").get() != None or jogo.css(".product-card--grid .icon-ios").get() != None:
                plataforma.append("mobile")

            if  jogo.css(".product-card--grid .icon-steam").get() != None or jogo.css(".product-card--grid .icon-windows").get() != None or jogo.css(".product-card--grid .icon-linux").get() != None or jogo.css(".product-card--grid .icon-mac").get() != None:
                plataforma.append("pc")

            preco = f"{moeda}{inteiro}{decimal}" if (moeda != None and inteiro != None and decimal != None) else "Indisponivel"
            yield {
                "nome": jogo.css('.product-card--grid .double-line-name::text').get() or jogo.css('.product-card--grid .single-line-name::text').get() ,
                "porcentagem_desconto": jogo.css('.product-card--grid .product-price--discount::text').get() or "0",
                "preço": preco,
                "tipo": jogo.css('.product-card--grid .product-badge__preorder::text').get() or jogo.css('.product-card--grid .product-badge__dlc::text').get() or jogo.css('.product-card--grid .product-badge__package::text').get() or "Padrão",
                "sistema": sistema,
                "plataforma": plataforma
            }
        pass
