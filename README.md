# Web Scraping com Scrapy 
## (books.toscrape.com)

### O que este código faz?
Este código é um exemplo do uso do framework <a href="www.scrapy.org">Scrapy</a> para fazer o web scraping de todos os livros na página <a href="https://books.toscrape.com/catalogue/page-1.html">books.toscrape.com</a>

### Como usar este código?
<ol>
    <li>
        Baixe este repositório para seu computador
    </li>
    <li>
        Crie um ambiente virtual para Python:<br/>
        <code>$ python3 -m venv venv</code>
    </li>
    <li>
        Instale as dependências:<br/>
        <code>$ pip install -r requirements.txt</code>
    </li>
</ol>

Feito isso você já terá o Scrapy instalado no seu ambiente virtual e pronto para rodar a spider
<br/><br/>

### Como rodar o spider?

O spider <i>books</i> é o responsável pelo web scraping em questão; para rodar ele e jogar a saida num arquivo json faça:

```bash
$ scrapy crawl books -O books_teste.json
```