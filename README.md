# gogoanime-anime-downloader
Downloads anime from [Gogoanime](https://www.gogoanime.lu).

## USAGE
* Input anime name as it is on [Gogoanime](https://www.gogoanime.lu) website (ex: use "Death Note", not "death note"). Anime name is case sensitive.
* To download dubbed version add "(Dub)" to the anime name (ex: use "Shingeki no Kyojin (Dub)")
* If some episodes link fails, download manually.

## Requirements
* Should have python installed
* Should have selenium installed 
  * Run command in terminal:
  * ```python
    pip install selenium
    ```
* Need to have a [Gogoanime](https://www.gogoanime.lu) account, if not make one.
* Should have [**wget installed**](https://www.gnu.org/software/wget/)

## Setting up selenium
* After installing selenium via pip, Download [selenium browser driver](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#quick-reference).
* Use this [article](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#2-the-path-environment-variable) to setup browser drivers in path (for linux, mac and windows)

## Editing data.json
Please fill-in the data.json with :
 * username
 * password
 * absolute path to the firefox extensions (ex: C:\Users\MyName\Desktop\gogoanime-anime-downloader\firefox_extensions\ublock_origin.xpi)
