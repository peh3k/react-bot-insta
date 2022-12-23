# Bot de Reação

![alt text](https://github.com/peh3k/Bot-Reacao/blob/main/bot.png)

![GitHub language count](https://img.shields.io/github/languages/count/peh3k/conversor-de-bases-numericas?style=for-the-badge)

> Esse é um **Bot** para **Instagram**, que usa um sistema automatizado para enviar **reações** ilimitadas nos stories de algum usuário

## Bibliotecas utilizadas

- `<Selenium>`
- `<PySimpleGui>`

## 💻 Pré-requisitos

Antes de começar, **verifique** se você atendeu aos seguintes requisitos:
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Possuir a versão mais recente de `<Python>` em sua máquina
* Possuir `<PyCharm / VsCode / Outros>`

## 🚀 Instalando PySimpleGui

Para instalar o *PySimpleGui*, siga estas etapas:

**Linux:**
```
pip install pysimplegui
```

**Windows:**
```
pip install pysimplegui
```
## 🚀 Instalando Selenium

Para instalar o *Selenium*, siga estas etapas:

**Linux:**
```
pip install selenium
```

**Windows:**
```
pip install selenium
```
## 🚀 Instalando WebDriver Chrome

Para instalar o *WebDriver* do Chrome, siga estas etapas:

- Baixe o arquivo compatível com a versão do seu Chrome<a href="https://chromedriver.chromium.org/downloads">WebDriver Chrome</a>
- Extraia os arquivos

**Linux:**

  Dentro da mesma pasta do arquivo extraído digite o comando:

```
sudo mv chomedriver /usr/local/bin/
```
**Windows:**

- Crie uma pasta
- Mova o arquivo "chromedriver.exe" para esta pasta
- Inicie o VsCode nesta mesma pasta
- Modifique de:
```
self.pagina = webdriver.Chrome()
```
para:
```
self.pagina = webdriver.Chrome('./chromedriver.exe')
```
Pronto agora é só rodar

## ❗ Observações Importantes ❗
- Como no programa foi utilizado **XPATH** do HTML,
o Instagram poderá modificar futuramente, assim tendo que atualizar
o código
- Caso apareça *PopUps* feche-os, caso contrário o código não
vai funcionar corretamente
- Copie a mensagem que o Bot irá enviar e deixe-a copiada
- O programa só funciona com a tela do Chrome aberta

### Author <a href="https://github.com/peh3k">peh3k</a>

[⬆ Voltar ao topo](#Bot-Reacao)<br>
