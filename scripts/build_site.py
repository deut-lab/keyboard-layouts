"""Build the static site in docs/ for four languages.

Usage: python scripts/build_site.py
English goes to docs/index.html, other languages to docs/<lang>/index.html.
"""
import os
import sys
from html import escape

sys.path.insert(0, os.path.dirname(__file__))
from added import HEAD, COLS, ROWS  # noqa: E402

REPO = "https://github.com/deut-lab/keyboard-layouts"
DL = REPO + "/releases/latest/download/"
LANGS = [("en", "English"), ("de", "Deutsch"), ("uk", "Українська"), ("ru", "Русский")]
VERSION_DATE = {"en": "17 Nov 2026", "de": "17.11.2026", "uk": "17.11.2026", "ru": "17.11.2026"}

T = {
"en": dict(
    title="RuUa and EnDe keyboard layouts",
    desc="Two free Windows keyboard layouts: Russian with Ukrainian letters and English with German letters.",
    h1="Two layouts, four languages",
    lead="An English layout that also has the German letters, and a Russian layout that also has the Ukrainian ones. Letters stay where you are used to them; everything extra is typed with the right Alt key. For Windows, free of charge.",
    dl_ruua="Download RuUa: Russian and Ukrainian", dl_ende="Download EnDe: English and German",
    note="Version 2611 of {date} · Windows 10 and 11 · <a href=\"#install\">how to install</a>",
    look="What they look like",
    look_sub="Each key shows up to four characters: bottom left is the key itself, top left is with Shift, blue on the right is with the right Alt key (the upper one also needs Shift).",
    alt_ruua="RuUa2611 layout: Russian ЙЦУКЕН letters; with the right Alt key the Ukrainian ґ, і, ї, є, the letter ё, currency signs, arrows and symbols",
    alt_ende="EnDe2611 layout: QWERTY letters; with the right Alt key the German ä, ö, ü, ß, quotes „“ and the accent keys ´ and ˇ",
    lg_black="<b>Black</b> is typed without Alt", lg_blue="<b>Blue</b> is typed with the right Alt key",
    lg_orange="<b>Orange</b>: press it, then a letter, and e becomes é", lg_nbsp="“nbsp” is a non-breaking space, “nnbsp” a narrow one",
    why="Why it is laid out this way",
    cards=[
     ("Nothing to relearn", "Letters stay in place", "ЙЦУКЕН and QWERTY are unchanged. Everything new sits on the right Alt key only, so your hands type as before from the first minute."),
     ("No third layout", "Ukrainian letters next to similar ones", "<kbd>ґ</kbd> on Г, <kbd>і</kbd> on Ы, <kbd>ї</kbd> on Ъ, <kbd>є</kbd> on Э, all with the right Alt key. Russian and Ukrainian live in one layout, no switching between them."),
     ("German without switching", "Umlauts on their own letters", "<kbd>ä</kbd> on A, <kbd>ö</kbd> on O, <kbd>ü</kbd> on U, <kbd>ß</kbd> on S. German quotes <kbd>„“</kbd> sit on the right Alt key next to the brackets, guillemets « » on the key beside them."),
     ("Same in both", "Punctuation does not jump", "Full stop and comma share one key, right of Ю, in both layouts. The symbols above the digits match too. Switch the language and your fingers find the same place."),
     ("Money and paperwork", "€, ₴, №, § on the digits", "With the right Alt key: <kbd>€</kbd> on 5, <kbd>₴</kbd> on 9, <kbd>№</kbd> on 3, <kbd>§</kbd> on 1, <kbd>@</kbd> on 2. With Shift and the right Alt key you get superscripts: m², m³."),
     ("Neat text", "Spaces that keep words together", "Right Alt plus space gives a non-breaking space, so “10 €” never splits across lines. With Shift you get a narrow one for “1 000” and “z. B.”."),
     ("Names from many countries", "é, á, š, č in two keystrokes", "In EnDe: Shift, right Alt and <kbd>'</kbd>, then a letter gives é, á, ó. Shift, right Alt and <kbd>M</kbd>, then a letter gives š, č, ž. For René, José, Dvořák."),
     ("For dictation", "The key left of 1 is free", "It types the rare character <kbd>ʹ</kbd>, which never appears in normal text, so it is a good key for starting voice input. The usual apostrophe is on the same key with Shift."),
     ("For forms and lists", "Check boxes, arrows, fractions", "<kbd>☐</kbd> <kbd>☑</kbd> <kbd>☒</kbd> <kbd>✔</kbd> on Z, X, J, arrows <kbd>→</kbd> <kbd>←</kbd> <kbd>↑</kbd> <kbd>↓</kbd>, fractions <kbd>½</kbd> <kbd>¾</kbd> on the top letter row."),
    ],
    install="How to install",
    steps=[
     'Download the archive of the layout you need with a button at the top and unpack it into any folder. After the installation you can delete that folder.',
     'Run <b>setup.exe</b>.',
     'When Windows asks for administrator rights, allow it.',
     'Open Settings, then “Time &amp; language” and “Language &amp; region”.',
     'Next to your language press “…”, then “Language options” and “Add a keyboard”.',
     'Choose <b>Russia-Ua 20261117</b> (for Russian) or <b>LAT-DEU 20261117</b> (for English).',
     'If the layout is not in the list yet, sign out of Windows and sign in again.',
    ],
    warn="If Windows says “Windows protected your PC”, click “More info” and “Run anyway”. It appears because the installer has no paid digital signature. The layouts do not work on computers with ARM processors (Snapdragon, Surface Pro X).",
    remove="To remove a layout, open Settings, then “Apps” and “Installed apps”, find its name and click “Uninstall”.",
    footer="Deut-lab · {lic} · <a href=\"" + REPO + "\">source on GitHub</a>, the .klc files open in Microsoft Keyboard Layout Creator 1.4.",
),
"de": dict(
    title="Tastaturlayouts RuUa und EnDe",
    desc="Zwei kostenlose Tastaturlayouts für Windows: Russisch mit ukrainischen Buchstaben und Englisch mit deutschen Buchstaben.",
    h1="Zwei Layouts, vier Sprachen",
    lead="Ein englisches Layout, das auch die deutschen Buchstaben hat, und ein russisches, das auch die ukrainischen hat. Die Buchstaben bleiben, wo Sie sie gewohnt sind; alles Zusätzliche tippen Sie mit der rechten Alt-Taste. Für Windows, kostenlos.",
    dl_ruua="RuUa herunterladen: Russisch und Ukrainisch", dl_ende="EnDe herunterladen: Englisch und Deutsch",
    note="Version 2611 vom {date} · Windows 10 und 11 · <a href=\"#install\">Installation</a>",
    look="So sehen sie aus",
    look_sub="Jede Taste zeigt bis zu vier Zeichen: unten links die Taste selbst, oben links mit Umschalt, rechts in Blau mit der rechten Alt-Taste (das obere zusätzlich mit Umschalt).",
    alt_ruua="Layout RuUa2611: russische Buchstaben ЙЦУКЕН; mit der rechten Alt-Taste die ukrainischen ґ, і, ї, є, der Buchstabe ё, Währungszeichen, Pfeile und Symbole",
    alt_ende="Layout EnDe2611: QWERTY-Buchstaben; mit der rechten Alt-Taste ä, ö, ü, ß, Anführungszeichen „“ und die Akzenttasten ´ und ˇ",
    lg_black="<b>Schwarz</b> ohne Alt", lg_blue="<b>Blau</b> mit der rechten Alt-Taste",
    lg_orange="<b>Orange</b>: erst diese Taste, dann ein Buchstabe, aus e wird é", lg_nbsp="„nbsp“ ist ein geschütztes Leerzeichen, „nnbsp“ ein schmales",
    why="Warum so",
    cards=[
     ("Nichts umlernen", "Buchstaben bleiben, wo sie sind", "ЙЦУКЕН und QWERTY sind unverändert. Alles Neue liegt nur auf der rechten Alt-Taste, die Hände tippen von der ersten Minute an wie gewohnt."),
     ("Kein drittes Layout", "Ukrainische Buchstaben neben ähnlichen", "<kbd>ґ</kbd> auf Г, <kbd>і</kbd> auf Ы, <kbd>ї</kbd> auf Ъ, <kbd>є</kbd> auf Э, jeweils mit der rechten Alt-Taste. Russisch und Ukrainisch in einem Layout, ohne Umschalten."),
     ("Deutsch ohne Umschalten", "Umlaute auf ihren Buchstaben", "<kbd>ä</kbd> auf A, <kbd>ö</kbd> auf O, <kbd>ü</kbd> auf U, <kbd>ß</kbd> auf S. Deutsche Anführungszeichen <kbd>„“</kbd> liegen mit der rechten Alt-Taste neben den Klammern, « » auf der Nachbartaste."),
     ("In beiden gleich", "Satzzeichen springen nicht", "Punkt und Komma liegen in beiden Layouts auf einer Taste rechts von Ю. Auch die Zeichen über den Ziffern stimmen überein. Sprache wechseln, die Finger finden dieselbe Stelle."),
     ("Geld und Papierkram", "€, ₴, №, § auf den Ziffern", "Mit der rechten Alt-Taste: <kbd>€</kbd> auf 5, <kbd>₴</kbd> auf 9, <kbd>№</kbd> auf 3, <kbd>§</kbd> auf 1, <kbd>@</kbd> auf 2. Mit Umschalt und rechter Alt-Taste Hochzahlen: m², m³."),
     ("Saubere Texte", "Leerzeichen, die nicht umbrechen", "Rechte Alt-Taste und Leertaste ergeben ein geschütztes Leerzeichen, „10 €“ wird nie getrennt. Mit Umschalt ein schmales für „1 000“ und „z. B.“."),
     ("Namen aus vielen Ländern", "é, á, š, č mit zwei Anschlägen", "In EnDe: Umschalt, rechte Alt-Taste und <kbd>'</kbd>, dann ein Buchstabe ergibt é, á, ó. Umschalt, rechte Alt-Taste und <kbd>M</kbd>, dann ein Buchstabe ergibt š, č, ž. Für René, José, Dvořák."),
     ("Für Diktat", "Die Taste links der 1 ist frei", "Sie tippt das seltene Zeichen <kbd>ʹ</kbd>, das in normalem Text nicht vorkommt, darum eignet sie sich zum Starten der Spracheingabe. Der übliche Apostroph liegt mit Umschalt auf derselben Taste."),
     ("Für Formulare und Listen", "Kästchen, Pfeile, Brüche", "<kbd>☐</kbd> <kbd>☑</kbd> <kbd>☒</kbd> <kbd>✔</kbd> auf Z, X, J, Pfeile <kbd>→</kbd> <kbd>←</kbd> <kbd>↑</kbd> <kbd>↓</kbd>, Brüche <kbd>½</kbd> <kbd>¾</kbd> in der oberen Buchstabenreihe."),
    ],
    install="Installation",
    steps=[
     'Laden Sie das Archiv des gewünschten Layouts über die Schaltfläche oben herunter und entpacken Sie es in einen beliebigen Ordner. Nach der Installation können Sie den Ordner löschen.',
     'Starten Sie <b>setup.exe</b>.',
     'Wenn Windows nach Administratorrechten fragt, stimmen Sie zu.',
     'Öffnen Sie „Einstellungen“, dann „Zeit und Sprache“ und „Sprache und Region“.',
     'Neben Ihrer Sprache „…“, dann „Sprachoptionen“ und „Tastatur hinzufügen“.',
     'Wählen Sie <b>Russia-Ua 20261117</b> (für Russisch) oder <b>LAT-DEU 20261117</b> (für Englisch).',
     'Fehlt das Layout noch in der Liste, melden Sie sich bei Windows ab und wieder an.',
    ],
    warn="Wenn Windows „Der Computer wurde durch Windows geschützt“ meldet, klicken Sie auf „Weitere Informationen“ und „Trotzdem ausführen“. Die Meldung erscheint, weil der Installer keine kostenpflichtige digitale Signatur hat. Auf Computern mit ARM-Prozessor (Snapdragon, Surface Pro X) funktionieren die Layouts nicht.",
    remove="Zum Entfernen öffnen Sie „Einstellungen“, dann „Apps“ und „Installierte Apps“, suchen den Namen des Layouts und klicken auf „Deinstallieren“.",
    footer="Deut-lab · {lic} · <a href=\"" + REPO + "\">Quellen auf GitHub</a>, die .klc-Dateien öffnen sich in Microsoft Keyboard Layout Creator 1.4.",
),
"uk": dict(
    title="Розкладки RuUa та EnDe",
    desc="Дві безкоштовні розкладки клавіатури для Windows: російська з українськими літерами та англійська з німецькими.",
    h1="Дві розкладки, чотири мови",
    lead="Російська розкладка, у якій є й українські літери, та англійська, у якій є й німецькі. Літери на звичних місцях, а все додаткове набирається з правим Alt. Для Windows, безкоштовно.",
    dl_ruua="Завантажити RuUa: російська й українська", dl_ende="Завантажити EnDe: англійська й німецька",
    note="Версія 2611 від {date} · Windows 10 і 11 · <a href=\"#install\">як встановити</a>",
    look="Як вони виглядають",
    look_sub="На кожній клавіші до чотирьох знаків: унизу ліворуч знак самої клавіші, угорі ліворуч знак із Shift, праворуч синім знаки з правим Alt (верхній ще й із Shift).",
    alt_ruua="Розкладка RuUa2611: російські літери ЙЦУКЕН; з правим Alt українські ґ, і, ї, є, літера ё, знаки валют, стрілки й символи",
    alt_ende="Розкладка EnDe2611: літери QWERTY; з правим Alt німецькі ä, ö, ü, ß, лапки „“ і клавіші наголосу ´ та ˇ",
    lg_black="<b>Чорним</b> набирається без Alt", lg_blue="<b>Синім</b> набирається з правим Alt",
    lg_orange="<b>Помаранчевим</b>: спершу цей знак, потім літера, і з e вийде é", lg_nbsp="«nbsp» означає нерозривний пробіл, «nnbsp» вузький",
    why="Чому саме так",
    cards=[
     ("Нічого не перевчати", "Літери на своїх місцях", "ЙЦУКЕН і QWERTY не змінені. Усе нове додано лише на правий Alt, тож руки друкують як раніше з першої хвилини."),
     ("Без третьої розкладки", "Українські літери поруч зі схожими", "<kbd>ґ</kbd> на Г, <kbd>і</kbd> на Ы, <kbd>ї</kbd> на Ъ, <kbd>є</kbd> на Э, усі з правим Alt. Російська й українська в одній розкладці, перемикатися не треба."),
     ("Німецька без перемикання", "Умлаути на своїх літерах", "<kbd>ä</kbd> на A, <kbd>ö</kbd> на O, <kbd>ü</kbd> на U, <kbd>ß</kbd> на S. Німецькі лапки <kbd>„“</kbd> стоять на правому Alt біля дужок, а «ялинки» на сусідній клавіші."),
     ("Однаково в обох", "Розділові знаки не стрибають", "Крапка й кома стоять на одній клавіші праворуч від Ю в обох розкладках. Знаки над цифрами теж збігаються. Перемкнули мову, а пальці шукають те саме місце."),
     ("Гроші й документи", "€, ₴, №, § на цифрах", "З правим Alt: <kbd>€</kbd> на 5, <kbd>₴</kbd> на 9, <kbd>№</kbd> на 3, <kbd>§</kbd> на 1, <kbd>@</kbd> на 2. Із Shift і правим Alt набираються степені: м², м³."),
     ("Охайний текст", "Пробіли, що не рвуть рядок", "Правий Alt і пробіл дають нерозривний пробіл, тож «10 €» не розійдеться по рядках. Із Shift вийде вузький: «1 000», «z. B.»."),
     ("Імена з різних країн", "é, á, š, č двома натисканнями", "В EnDe: Shift, правий Alt і <kbd>'</kbd>, потім літера, і вийде é, á, ó. Shift, правий Alt і <kbd>M</kbd>, потім літера, і вийде š, č, ž. Для René, José, Dvořák."),
     ("Для диктування", "Клавіша біля 1 вільна", "Вона друкує рідкісний знак <kbd>ʹ</kbd>, якого немає у звичайному тексті, тому на неї зручно повісити виклик голосового введення. Звичайний апостроф набирається із Shift на тій самій клавіші."),
     ("Для форм і списків", "Позначки, стрілки, дроби", "<kbd>☐</kbd> <kbd>☑</kbd> <kbd>☒</kbd> <kbd>✔</kbd> на Z, X, J, стрілки <kbd>→</kbd> <kbd>←</kbd> <kbd>↑</kbd> <kbd>↓</kbd>, дроби <kbd>½</kbd> <kbd>¾</kbd> у верхньому ряду літер."),
    ],
    install="Як встановити",
    steps=[
     'Завантажте архів потрібної розкладки кнопкою вгорі сторінки й розпакуйте його в будь-яку папку. Після встановлення цю папку можна видалити.',
     'Запустіть <b>setup.exe</b>.',
     'Коли Windows попросить права адміністратора, погодьтеся.',
     'Відкрийте «Параметри», потім «Час і мова» та «Мова й регіон».',
     'Біля потрібної мови натисніть «…», потім «Параметри мови» та «Додати клавіатуру».',
     'Виберіть <b>Russia-Ua 20261117</b> (для російської) або <b>LAT-DEU 20261117</b> (для англійської).',
     'Якщо розкладки ще немає в списку, вийдіть з облікового запису Windows і увійдіть знову.',
    ],
    warn="Якщо Windows пише «Windows захистила ваш ПК», натисніть «Докладніше» і «Усе одно запустити». Попередження з’являється тому, що в інсталятора немає платного цифрового підпису. На комп’ютерах із процесором ARM (Snapdragon, Surface Pro X) розкладки не працюють.",
    remove="Щоб видалити, відкрийте «Параметри», потім «Програми» та «Інстальовані програми», знайдіть назву розкладки й натисніть «Видалити».",
    footer="Deut-lab · {lic} · <a href=\"" + REPO + "\">вихідні файли на GitHub</a>, файли .klc відкриваються в Microsoft Keyboard Layout Creator 1.4.",
),
"ru": dict(
    title="Раскладки RuUa и EnDe",
    desc="Две бесплатные раскладки клавиатуры для Windows: русская с украинскими буквами и английская с немецкими.",
    h1="Две раскладки, четыре языка",
    lead="Русская раскладка с украинскими буквами и английская с немецкими. Буквы на привычных местах, а всё дополнительное набирается с правым Alt. Для Windows, бесплатно.",
    dl_ruua="Скачать RuUa: русский и украинский", dl_ende="Скачать EnDe: английский и немецкий",
    note="Версия 2611 от {date} · Windows 10 и 11 · <a href=\"#install\">как установить</a>",
    look="Как выглядят",
    look_sub="На каждой клавише до четырёх знаков: внизу слева знак самой клавиши, вверху слева знак с Shift, справа синим знаки с правым Alt (верхний набирается ещё и с Shift).",
    alt_ruua="Раскладка RuUa2611: русские буквы ЙЦУКЕН; с правым Alt украинские ґ, і, ї, є, буква ё, валюты, стрелки и знаки",
    alt_ende="Раскладка EnDe2611: буквы QWERTY; с правым Alt немецкие ä, ö, ü, ß, кавычки „“ и клавиши ударения ´ и ˇ",
    lg_black="<b>Чёрным</b> набирается без Alt", lg_blue="<b>Синим</b> набирается с правым Alt",
    lg_orange="<b>Оранжевым</b>: сначала этот знак, потом буква, и из e выйдет é", lg_nbsp="«nbsp» значит неразрывный пробел, «nnbsp» узкий",
    why="Почему так",
    cards=[
     ("Ничего не переучивать", "Буквы на своих местах", "ЙЦУКЕН и QWERTY остались как были. Всё новое добавлено только на правый Alt, поэтому руки печатают по-старому с первой минуты."),
     ("Без третьей раскладки", "Украинские буквы рядом с похожими", "<kbd>ґ</kbd> на Г, <kbd>і</kbd> на Ы, <kbd>ї</kbd> на Ъ, <kbd>є</kbd> на Э, все с правым Alt. Русский и украинский в одной раскладке, переключаться между ними не нужно."),
     ("Немецкий без переключения", "Умлауты на своих буквах", "<kbd>ä</kbd> на A, <kbd>ö</kbd> на O, <kbd>ü</kbd> на U, <kbd>ß</kbd> на S. Немецкие кавычки <kbd>„“</kbd> стоят на правом Alt рядом со скобками, а «ёлочки» на соседней клавише."),
     ("Одинаково в обеих", "Знаки не прыгают при смене языка", "Точка и запятая стоят на одной клавише справа от Ю в обеих раскладках. Знаки над цифрами тоже совпадают. Переключили язык, а пальцы ищут то же место."),
     ("Деньги и документы", "€, ₴, №, § на цифрах", "С правым Alt: <kbd>€</kbd> на 5, <kbd>₴</kbd> на 9, <kbd>№</kbd> на 3, <kbd>§</kbd> на 1, <kbd>@</kbd> на 2. С Shift и правым Alt набираются степени: м², м³."),
     ("Красивый текст", "Пробелы, которые не рвут строку", "Правый Alt и пробел дают неразрывный пробел, поэтому «10 €» не разъедется по строкам. С Shift получится узкий: «1 000», «z. B.»."),
     ("Имена из разных стран", "é, á, š, č двумя нажатиями", "В EnDe: Shift, правый Alt и <kbd>'</kbd>, затем буква, и выйдет é, á, ó. Shift, правый Alt и <kbd>M</kbd>, затем буква, и выйдет š, č, ž. Для René, José, Dvořák."),
     ("Для диктовки", "Клавиша у единицы свободна", "Она печатает редкий знак <kbd>ʹ</kbd>, которого нет в обычном тексте, поэтому на неё удобно повесить вызов голосового ввода. Обычный апостроф набирается с Shift на той же клавише."),
     ("Для форм и списков", "Галочки, стрелки, дроби", "<kbd>☐</kbd> <kbd>☑</kbd> <kbd>☒</kbd> <kbd>✔</kbd> на Z, X, J, стрелки <kbd>→</kbd> <kbd>←</kbd> <kbd>↑</kbd> <kbd>↓</kbd>, дроби <kbd>½</kbd> <kbd>¾</kbd> на верхнем ряду букв."),
    ],
    install="Как установить",
    steps=[
     'Скачайте архив нужной раскладки кнопкой вверху страницы и распакуйте его в любую папку. После установки эту папку можно удалить.',
     'Запустите <b>setup.exe</b>.',
     'Когда Windows попросит права администратора, согласитесь.',
     'Откройте «Параметры», затем «Время и язык» и «Язык и регион».',
     'У нужного языка нажмите «…», затем «Параметры языка» и «Добавить клавиатуру».',
     'Выберите <b>Russia-Ua 20261117</b> (для русского) или <b>LAT-DEU 20261117</b> (для английского).',
     'Если раскладки ещё нет в списке, выйдите из учётной записи Windows и войдите снова.',
    ],
    warn="Если Windows пишет «Система Windows защитила ваш компьютер», нажмите «Подробнее» и «Выполнить в любом случае». Предупреждение появляется потому, что у установщика нет платной цифровой подписи. На компьютерах с процессором ARM (Snapdragon, Surface Pro X) раскладки не работают.",
    remove="Чтобы удалить, откройте «Параметры», затем «Приложения» и «Установленные приложения», найдите название раскладки и нажмите «Удалить».",
    footer="Deut-lab · {lic} · <a href=\"" + REPO + "\">исходники на GitHub</a>, файлы .klc открываются в Microsoft Keyboard Layout Creator 1.4.",
),
}

PKG = {'en': 'The archive was built with the standard Microsoft application Keyboard Layout Creator and contains Windows installation files:<ul><li><b>setup.exe</b>: starts the installation and picks the right file by itself;</li><li><b>…_amd64.msi</b>: installer for ordinary 64-bit computers with Intel or AMD processors;</li><li><b>…_i386.msi</b>: installer for old 32-bit Windows;</li><li><b>…_ia64.msi</b>: installer for Itanium servers, not needed on ordinary computers;</li><li>folders <b>amd64, i386, ia64, wow64</b>: the layout files themselves for each kind of Windows (wow64 serves 32-bit programs on 64-bit Windows); they are not run separately.</li></ul>To install, run <b>setup.exe</b>.', 'de': 'Das Archiv wurde mit der Standardanwendung Keyboard Layout Creator von Microsoft erstellt und enthält Installationsdateien für Windows:<ul><li><b>setup.exe</b>: startet die Installation und wählt die passende Datei selbst;</li><li><b>…_amd64.msi</b>: Installer für gewöhnliche 64-Bit-Computer mit Intel- oder AMD-Prozessor;</li><li><b>…_i386.msi</b>: Installer für altes 32-Bit-Windows;</li><li><b>…_ia64.msi</b>: Installer für Itanium-Server, auf gewöhnlichen Computern nicht nötig;</li><li>Ordner <b>amd64, i386, ia64, wow64</b>: die Layoutdateien selbst für jede Windows-Art (wow64 für 32-Bit-Programme auf 64-Bit-Windows); sie werden nicht einzeln gestartet.</li></ul>Zum Installieren starten Sie <b>setup.exe</b>.', 'uk': 'Архів зібрано стандартною програмою Microsoft Keyboard Layout Creator, він містить інсталяційні файли для Windows:<ul><li><b>setup.exe</b>: запускає встановлення й сам вибирає потрібний файл;</li><li><b>…_amd64.msi</b>: інсталятор для звичайних 64-бітних комп’ютерів із процесором Intel або AMD;</li><li><b>…_i386.msi</b>: інсталятор для старих 32-бітних Windows;</li><li><b>…_ia64.msi</b>: інсталятор для серверів Itanium, на звичайних комп’ютерах не потрібен;</li><li>папки <b>amd64, i386, ia64, wow64</b>: самі файли розкладки для кожного виду Windows (wow64 потрібна 32-бітним програмам на 64-бітній Windows); окремо їх запускати не треба.</li></ul>Щоб встановити, запустіть <b>setup.exe</b>.', 'ru': 'Архив собран стандартным приложением Microsoft Keyboard Layout Creator и содержит установочные файлы для Windows:<ul><li><b>setup.exe</b>: запускает установку и сам выбирает нужный файл;</li><li><b>…_amd64.msi</b>: установщик для обычных 64-битных компьютеров с процессором Intel или AMD;</li><li><b>…_i386.msi</b>: установщик для старых 32-битных Windows;</li><li><b>…_ia64.msi</b>: установщик для серверов Itanium, на обычных компьютерах не нужен;</li><li>папки <b>amd64, i386, ia64, wow64</b>: сами файлы раскладки для каждого вида Windows (wow64 нужна 32-битным программам на 64-битной Windows); отдельно их запускать не нужно.</li></ul>Для запуска нажмите <b>setup.exe</b>.'}

LICENSE_NAME = '<a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a>'

CSS = open(os.path.join(os.path.dirname(__file__), "site.css"), encoding="utf-8").read()


def page(lang):
    t = T[lang]
    root = "" if lang == "en" else "../"
    menu = "".join(
        f'<a href="{root}{"" if code == "en" else code + "/"}" hreflang="{code}" lang="{code}"'
        + (' aria-current="page"' if code == lang else "") + f">{name}</a>"
        for code, name in LANGS)
    alternates = "".join(
        f'<link rel="alternate" hreflang="{code}" href="https://deut-lab.github.io/keyboard-layouts/{"" if code == "en" else code + "/"}">'
        for code, _ in LANGS)
    ende_first = lang in ("en", "de")
    card_list = list(t["cards"])
    if ende_first:
        card_list[1], card_list[2] = card_list[2], card_list[1]
    cards = "".join(
        f'<div class="item"><span class="tag">{tag}</span><h3>{h}</h3><p>{p}</p></div>'
        for tag, h, p in card_list)
    row_list = sorted(ROWS, key=lambda r: r[0] == "RuUa") if ende_first else ROWS
    steps = "".join(f"<li>{s}</li>" for s in t["steps"])
    h_title, h_sub = HEAD[lang]
    c1, c2, c3 = COLS[lang]
    rows = "".join(
        f'<div class="row"><div class="chars">{escape(ch)}<span class="lay">{lay}</span></div>'
        f'<div class="where"><span class="lbl">{c2}</span>{escape(where[lang])}</div>'
        f'<div class="whyc"><span class="lbl">{c3}</span>{escape(why[lang])}</div></div>'
        for lay, ch, where, why in row_list)
    order = ["ende", "ruua"] if ende_first else ["ruua", "ende"]
    names = {"ruua": "RuUa", "ende": "EnDe"}
    buttons = "".join(
        f'<a class="btn {"primary" if i == 0 else "tonal"}" href="{DL}{names[k]}2611.zip">{t["dl_" + k]}</a>'
        for i, k in enumerate(order))
    tabs = "".join(
        f'<button role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="p-{k}" id="t-{k}">{names[k]}</button>'
        for i, k in enumerate(order))
    panels = "".join(
        f'<div class="panel" id="p-{k}" role="tabpanel" aria-labelledby="t-{k}"{"" if i == 0 else " hidden"}>'
        f'<div class="kbd-img"><img src="{root}img/{names[k]}2611.svg" alt="{escape(t["alt_" + k])}"></div></div>'
        for i, k in enumerate(order))
    added = (f'<section class="card" id="added"><h2>{h_title}</h2><p class="sub">{h_sub}</p>'
             f'<div class="added"><div class="row head"><div>{c1}</div><div>{c2}</div><div>{c3}</div></div>{rows}</div></section>')
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(t["title"])}</title>
<meta name="description" content="{escape(t["desc"])}">
{alternates}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap">
<style>{CSS}</style>
</head>
<body>
<nav class="top"><div class="wrap"><span class="brand">RuUa · EnDe</span><span class="langs">{menu}</span></div></nav>
<div class="wrap">
<header>
  <h1>{t["h1"]}</h1>
  <p class="lead">{t["lead"]}</p>
  <div class="btns">
{buttons}
  </div>
  <p class="note">{t["note"].format(date=VERSION_DATE[lang])}</p>
</header>
<section class="card">
  <h2>{t["look"]}</h2>
  <p class="sub">{t["look_sub"]}</p>
  <div class="tabs" role="tablist">
{tabs}
  </div>
{panels}
  <div class="legend"><span>{t["lg_black"]}</span><span class="c-alt">{t["lg_blue"]}</span><span class="c-dead">{t["lg_orange"]}</span><span>{t["lg_nbsp"]}</span></div>
</section>
<section><h2 class="why-title">{t["why"]}</h2><div class="why">{cards}</div></section>
{added}
<section class="card" id="install">
  <h2>{t["install"]}</h2>
  <div class="warn pkg">{PKG[lang]}</div>
  <ol class="steps">{steps}</ol>
  <div class="warn">{t["warn"]}</div>
  <p class="sub" style="margin-top:16px">{t["remove"]}</p>
</section>
<footer>{t["footer"].format(lic=LICENSE_NAME)}</footer>
</div>
<script>
  const tabs = document.querySelectorAll('[role="tab"]');
  tabs.forEach(t => t.addEventListener('click', () => {{
    tabs.forEach(o => {{ o.setAttribute('aria-selected', o === t); document.getElementById(o.getAttribute('aria-controls')).hidden = o !== t; }});
  }}));
</script>
</body>
</html>
"""


if __name__ == "__main__":
    base = os.path.join(os.path.dirname(__file__), "..", "docs")
    for code, _ in LANGS:
        out = base if code == "en" else os.path.join(base, code)
        os.makedirs(out, exist_ok=True)
        open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page(code))
    print("built:", ", ".join(c for c, _ in LANGS))
