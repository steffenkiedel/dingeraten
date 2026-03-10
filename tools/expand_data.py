#!/usr/bin/env python3
"""Expand all data files with new items."""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, 'data')

# ─── HAUPTSTÄDTE (new items) ────────────────────────────────────────────────
new_hauptstaedte = [
  {
    "id": "wien",
    "name": {"de": "Wien", "en": "Vienna"},
    "category": "hauptstaedte",
    "difficulty": 1,
    "facts": {"country": "Österreich", "country_en": "Austria", "continent": "Europa", "population_million": 1.9, "known_for": ["Stephansdom", "Schönbrunn", "Wiener Philharmoniker", "Sachertorte"], "language": "Deutsch"},
    "hints": [
      {"de": "Es ist die Hauptstadt von Österreich", "en": "It is the capital of Austria"},
      {"de": "Der Stephansdom ist das Wahrzeichen dieser Stadt", "en": "St. Stephen's Cathedral is the landmark of this city"},
      {"de": "Es ist bekannt für klassische Musik und Mozart", "en": "It is famous for classical music and Mozart"}
    ],
    "description": {"de": "Wien ist die Hauptstadt Österreichs und war einst das Zentrum des Habsburger Reiches. Die Stadt ist weltberühmt für ihre Musik, ihre Kaffeehäuser und den Stephansdom.", "en": "Vienna is the capital of Austria and was once the center of the Habsburg Empire. The city is world-famous for its music, coffee houses and St. Stephen's Cathedral."},
    "fun_fact": {"de": "Wien wurde mehrmals zur lebenswertesten Stadt der Welt gewählt! Außerdem ist Wien die einzige Hauptstadt, die zugleich ein eigenes Bundesland ist und Wein innerhalb der Stadtgrenzen anbaut.", "en": "Vienna has been voted the world's most liveable city multiple times! Also, Vienna is the only capital that is simultaneously its own federal state and grows wine within city limits."},
    "flag_url": "https://flagcdn.com/w320/at.png",
    "emoji": "🇦🇹",
    "qa_context": "Wien, Vienna, Hauptstadt Österreich, 1,9 Mio. Einwohner, Europa, bekannt für Stephansdom, Schönbrunn, Wiener Philharmoniker, Mozart, Sachertorte, Kaffeehäuser, Habsburger Reich, lebenswerteste Stadt der Welt"
  },
  {
    "id": "amsterdam",
    "name": {"de": "Amsterdam", "en": "Amsterdam"},
    "category": "hauptstaedte",
    "difficulty": 1,
    "facts": {"country": "Niederlande", "country_en": "Netherlands", "continent": "Europa", "population_million": 0.9, "known_for": ["Grachten", "Anne-Frank-Haus", "Rijksmuseum", "Fahrräder"], "language": "Niederländisch"},
    "hints": [
      {"de": "Es ist die Hauptstadt der Niederlande", "en": "It is the capital of the Netherlands"},
      {"de": "Es ist bekannt für seine vielen Grachten (Kanäle)", "en": "It is known for its many canals"},
      {"de": "Hier lebte Anne Frank und versteckte sich vor den Nazis", "en": "Anne Frank lived and hid from the Nazis here"}
    ],
    "description": {"de": "Amsterdam ist die Hauptstadt der Niederlande und bekannt für seine Grachten, Tulpen und Fahrräder. Das Anne-Frank-Haus und das Rijksmuseum sind wichtige Sehenswürdigkeiten.", "en": "Amsterdam is the capital of the Netherlands and known for its canals, tulips and bicycles. The Anne Frank House and Rijksmuseum are important sights."},
    "fun_fact": {"de": "In Amsterdam gibt es mehr Fahrräder als Einwohner! Mit über 880.000 Fahrrädern auf knapp 900.000 Einwohner ist Amsterdam die Fahrradhauptstadt der Welt.", "en": "Amsterdam has more bicycles than residents! With over 880,000 bikes for about 900,000 residents, Amsterdam is the bicycle capital of the world."},
    "flag_url": "https://flagcdn.com/w320/nl.png",
    "emoji": "🇳🇱",
    "qa_context": "Amsterdam, Hauptstadt Niederlande/Holland, 900.000 Einwohner, Europa, bekannt für Grachten (Kanäle), Anne-Frank-Haus, Rijksmuseum, Tulpen, Fahrräder (mehr Fahrräder als Menschen), Van Gogh Museum"
  },
  {
    "id": "stockholm",
    "name": {"de": "Stockholm", "en": "Stockholm"},
    "category": "hauptstaedte",
    "difficulty": 1,
    "facts": {"country": "Schweden", "country_en": "Sweden", "continent": "Europa", "population_million": 1.0, "known_for": ["ABBA", "Nobelpreis", "Vasa-Museum", "IKEA"], "language": "Schwedisch"},
    "hints": [
      {"de": "Es ist die Hauptstadt von Schweden", "en": "It is the capital of Sweden"},
      {"de": "Hier wird jedes Jahr der Nobelpreis verliehen", "en": "The Nobel Prize is awarded here every year"},
      {"de": "Es liegt auf 14 Inseln", "en": "It is built on 14 islands"}
    ],
    "description": {"de": "Stockholm ist die Hauptstadt Schwedens und liegt auf 14 Inseln. Hier wird jährlich der Nobelpreis verliehen. ABBA, IKEA und Spotify stammen alle aus Schweden.", "en": "Stockholm is the capital of Sweden and lies on 14 islands. The Nobel Prize is awarded here annually. ABBA, IKEA and Spotify all come from Sweden."},
    "fun_fact": {"de": "Stockholm ist die Geburtsstadt des ABBA-Museums und der App Spotify! Außerdem kommt IKEA aus Schweden — der Gründer Ingvar Kamprad benannte die Firma nach seinen Initialen und seinem Bauernhof.", "en": "Stockholm is the birthplace of the ABBA Museum and the app Spotify! Also, IKEA comes from Sweden — founder Ingvar Kamprad named the company after his initials and his farm."},
    "flag_url": "https://flagcdn.com/w320/se.png",
    "emoji": "🇸🇪",
    "qa_context": "Stockholm, Hauptstadt Schweden, 1 Mio. Einwohner, Nordeuropa, Europa, auf 14 Inseln, bekannt für Nobelpreis, ABBA, IKEA, Spotify, Vasa-Museum, Gamla Stan (Altstadt)"
  },
  {
    "id": "bern",
    "name": {"de": "Bern", "en": "Bern"},
    "category": "hauptstaedte",
    "difficulty": 2,
    "facts": {"country": "Schweiz", "country_en": "Switzerland", "continent": "Europa", "population_million": 0.14, "known_for": ["Bärengraben", "Zytglogge", "UNESCO Altstadt"], "language": "Deutsch, Französisch, Italienisch, Rätoromanisch"},
    "hints": [
      {"de": "Es ist die Hauptstadt der Schweiz", "en": "It is the capital of Switzerland"},
      {"de": "Viele denken, Zürich oder Genf ist die Hauptstadt — aber das stimmt nicht", "en": "Many think Zurich or Geneva is the capital — but that's wrong"},
      {"de": "Die Stadt hat ihren Namen vom Bären und hält echte Bären", "en": "The city got its name from bears and keeps real bears"}
    ],
    "description": {"de": "Bern ist die Hauptstadt der Schweiz, obwohl viele Zürich oder Genf vermuten. Die mittelalterliche Altstadt steht auf der UNESCO-Welterbeliste. Die Stadt hält echte Bären im Bärenpark.", "en": "Bern is the capital of Switzerland, although many guess Zurich or Geneva. The medieval old town is on the UNESCO World Heritage List. The city keeps real bears in Bear Park."},
    "fun_fact": {"de": "Bern ist nur die 4. größte Stadt der Schweiz, aber die Hauptstadt! Und tatsächlich hält die Stadt im Bärenpark echte Bären — denn das Wort 'Bern' soll vom altdeutschen Wort für Bär kommen.", "en": "Bern is only Switzerland's 4th largest city, but the capital! And the city actually keeps real bears in Bear Park — because the word 'Bern' is said to come from the old German word for bear."},
    "flag_url": "https://flagcdn.com/w320/ch.png",
    "emoji": "🇨🇭",
    "qa_context": "Bern, Hauptstadt Schweiz, 140.000 Einwohner, Europa, 4 Landessprachen (Deutsch/Französisch/Italienisch/Rätoromanisch), bekannt für Bärengraben, UNESCO Altstadt, oft mit Zürich verwechselt"
  },
  {
    "id": "athen",
    "name": {"de": "Athen", "en": "Athens"},
    "category": "hauptstaedte",
    "difficulty": 2,
    "facts": {"country": "Griechenland", "country_en": "Greece", "continent": "Europa", "population_million": 3.1, "known_for": ["Akropolis", "Parthenon", "Olympische Spiele", "Demokratie"], "language": "Griechisch"},
    "hints": [
      {"de": "Es ist die Hauptstadt von Griechenland", "en": "It is the capital of Greece"},
      {"de": "Die Akropolis mit dem Parthenon-Tempel steht hier", "en": "The Acropolis with the Parthenon temple is here"},
      {"de": "Hier wurden die ersten Olympischen Spiele der Neuzeit abgehalten", "en": "The first modern Olympic Games were held here"}
    ],
    "description": {"de": "Athen ist die Hauptstadt Griechenlands und eine der ältesten Städte der Welt. Die Akropolis mit dem Parthenon ist das bekannteste Symbol der Antike. Athen gilt als Wiege der Demokratie.", "en": "Athens is the capital of Greece and one of the oldest cities in the world. The Acropolis with the Parthenon is the most famous symbol of antiquity. Athens is considered the cradle of democracy."},
    "fun_fact": {"de": "Athen ist eine der ältesten bewohnten Städte der Welt — über 3.400 Jahre Geschichte! Die modernen Olympischen Spiele wurden 1896 in Athen wiederbelebt, genau dort, wo die antiken Spiele ihren Ursprung hatten.", "en": "Athens is one of the oldest inhabited cities in the world — over 3,400 years of history! The modern Olympic Games were revived in Athens in 1896, exactly where the ancient games originated."},
    "flag_url": "https://flagcdn.com/w320/gr.png",
    "emoji": "🇬🇷",
    "qa_context": "Athen, Athens, Hauptstadt Griechenland, 3,1 Mio. Einwohner, Europa, Mittelmeer, bekannt für Akropolis, Parthenon, Wiege der Demokratie, erste moderne Olympische Spiele 1896, sehr alte Stadt"
  },
  {
    "id": "peking",
    "name": {"de": "Peking", "en": "Beijing"},
    "category": "hauptstaedte",
    "difficulty": 2,
    "facts": {"country": "China", "country_en": "China", "continent": "Asien", "population_million": 21, "known_for": ["Verbotene Stadt", "Chinesische Mauer", "Tiananmen-Platz", "Peking-Oper"], "language": "Chinesisch (Mandarin)"},
    "hints": [
      {"de": "Es ist die Hauptstadt von China", "en": "It is the capital of China"},
      {"de": "Die Verbotene Stadt und der Tiananmen-Platz befinden sich hier", "en": "The Forbidden City and Tiananmen Square are here"},
      {"de": "Von hier aus beginnt der bekannteste Teil der Chinesischen Mauer", "en": "The most famous section of the Great Wall of China starts near here"}
    ],
    "description": {"de": "Peking (Beijing) ist die Hauptstadt Chinas mit 21 Millionen Einwohnern. Die Verbotene Stadt war über 500 Jahre kaiserlicher Palast. Die Chinesische Mauer ist in der Nähe.", "en": "Beijing is the capital of China with 21 million inhabitants. The Forbidden City was the imperial palace for over 500 years. The Great Wall of China is nearby."},
    "fun_fact": {"de": "Die Verbotene Stadt in Peking hat 9.999 Räume! Der Kaiser durfte als einziger dort wohnen — Besucher ohne Erlaubnis wurden mit dem Tod bestraft. Heute ist es das meistbesuchte Museum der Welt.", "en": "The Forbidden City in Beijing has 9,999 rooms! The emperor was the only one allowed to live there — visitors without permission were punished with death. Today it's the world's most visited museum."},
    "flag_url": "https://flagcdn.com/w320/cn.png",
    "emoji": "🇨🇳",
    "qa_context": "Peking, Beijing, Hauptstadt China, 21 Mio. Einwohner, Asien, Chinesisch/Mandarin, bekannt für Verbotene Stadt, Tiananmen-Platz, Chinesische Mauer in der Nähe, Peking-Ente, Peking-Oper"
  },
  {
    "id": "moskau",
    "name": {"de": "Moskau", "en": "Moscow"},
    "category": "hauptstaedte",
    "difficulty": 2,
    "facts": {"country": "Russland", "country_en": "Russia", "continent": "Europa/Asien", "population_million": 12, "known_for": ["Roter Platz", "Kreml", "Basilius-Kathedrale", "Metro"], "language": "Russisch"},
    "hints": [
      {"de": "Es ist die Hauptstadt von Russland", "en": "It is the capital of Russia"},
      {"de": "Der Rote Platz und der Kreml befinden sich hier", "en": "Red Square and the Kremlin are here"},
      {"de": "Es ist die größte Stadt Europas", "en": "It is the largest city in Europe"}
    ],
    "description": {"de": "Moskau ist die Hauptstadt Russlands und die größte Stadt Europas mit 12 Millionen Einwohnern. Der Kreml ist der Regierungssitz. Die bunten Zwiebeltürme der Basilius-Kathedrale prägen das Bild.", "en": "Moscow is the capital of Russia and the largest city in Europe with 12 million inhabitants. The Kremlin is the seat of government. The colorful onion domes of St. Basil's Cathedral define the image."},
    "fun_fact": {"de": "Die Moskauer Metro ist eine der schönsten und tiefsten der Welt! Viele Stationen sehen aus wie Museen — mit Marmor, Kronleuchtern und Mosaiken. Täglich fahren über 9 Millionen Menschen damit.", "en": "The Moscow Metro is one of the most beautiful and deepest in the world! Many stations look like museums — with marble, chandeliers and mosaics. Over 9 million people use it daily."},
    "flag_url": "https://flagcdn.com/w320/ru.png",
    "emoji": "🇷🇺",
    "qa_context": "Moskau, Moscow, Hauptstadt Russland, 12 Mio. Einwohner, größte Stadt Europas, Europa/Asien, Russisch, bekannt für Kreml, Roter Platz, Basilius-Kathedrale (bunte Zwiebeltürme), prächtige Metro"
  },
  {
    "id": "kairo",
    "name": {"de": "Kairo", "en": "Cairo"},
    "category": "hauptstaedte",
    "difficulty": 2,
    "facts": {"country": "Ägypten", "country_en": "Egypt", "continent": "Afrika", "population_million": 21, "known_for": ["Pyramiden von Gizeh", "Sphinx", "Nil", "Ägyptisches Museum"], "language": "Arabisch"},
    "hints": [
      {"de": "Es ist die Hauptstadt von Ägypten", "en": "It is the capital of Egypt"},
      {"de": "Die Pyramiden von Gizeh sind in der Nähe dieser Stadt", "en": "The Pyramids of Giza are near this city"},
      {"de": "Der Nil fließt durch diese Stadt", "en": "The Nile flows through this city"}
    ],
    "description": {"de": "Kairo ist die Hauptstadt Ägyptens und die größte Stadt Afrikas. Die Pyramiden von Gizeh und die Sphinx befinden sich am Rand der Stadt. Der Nil fließt durch Kairo.", "en": "Cairo is the capital of Egypt and the largest city in Africa. The Pyramids of Giza and the Sphinx are on the edge of the city. The Nile flows through Cairo."},
    "fun_fact": {"de": "Die Pyramide von Gizeh ist das einzige noch erhaltene Weltwunder der Antike! Sie wurde vor über 4.500 Jahren gebaut und war fast 4.000 Jahre lang das höchste Bauwerk der Welt.", "en": "The Great Pyramid of Giza is the only surviving wonder of the ancient world! It was built over 4,500 years ago and was the world's tallest structure for almost 4,000 years."},
    "flag_url": "https://flagcdn.com/w320/eg.png",
    "emoji": "🇪🇬",
    "qa_context": "Kairo, Cairo, Hauptstadt Ägypten, 21 Mio. Einwohner, größte Stadt Afrikas, Nordafrika, Arabisch, bekannt für Pyramiden von Gizeh, Sphinx, Nil, Ägyptisches Museum, sehr alte Zivilisation"
  },
  {
    "id": "brasilia",
    "name": {"de": "Brasília", "en": "Brasília"},
    "category": "hauptstaedte",
    "difficulty": 3,
    "facts": {"country": "Brasilien", "country_en": "Brazil", "continent": "Südamerika", "population_million": 3.1, "known_for": ["futuristische Architektur", "Nationalkathedrale", "neu gebaut 1960"], "language": "Portugiesisch"},
    "hints": [
      {"de": "Es ist die Hauptstadt von Brasilien", "en": "It is the capital of Brazil"},
      {"de": "Viele denken, Rio de Janeiro oder São Paulo ist die Hauptstadt — aber das ist falsch!", "en": "Many think Rio de Janeiro or São Paulo is the capital — but that's wrong!"},
      {"de": "Diese Stadt wurde mitten im Dschungel aus dem Nichts gebaut", "en": "This city was built from scratch in the middle of the jungle"}
    ],
    "description": {"de": "Brasília ist die Hauptstadt Brasiliens — nicht Rio de Janeiro! Die futuristische Stadt wurde von 1956 bis 1960 komplett neu im Landesinneren gebaut und ist UNESCO-Welterbe.", "en": "Brasília is the capital of Brazil — not Rio de Janeiro! The futuristic city was completely newly built inland from 1956 to 1960 and is a UNESCO World Heritage Site."},
    "fun_fact": {"de": "Brasília ist eine der wenigen Hauptstädte der Welt, die komplett neu gebaut wurden! In nur 4 Jahren (1956-1960) entstand eine ganze Stadt — von Null. Das Stadtbild hat die Form eines Flugzeugs, wenn man es von oben sieht.", "en": "Brasília is one of the few capitals in the world that was completely built from scratch! In just 4 years (1956-1960) an entire city emerged — from zero. The city layout has the shape of an airplane when seen from above."},
    "flag_url": "https://flagcdn.com/w320/br.png",
    "emoji": "🇧🇷",
    "qa_context": "Brasília, Brasilia, Hauptstadt Brasilien, 3,1 Mio. Einwohner, Südamerika, Portugiesisch, futuristische Architektur, neu gebaut 1960, oft mit Rio de Janeiro verwechselt, UNESCO Welterbe, Stadtform wie Flugzeug"
  },
  {
    "id": "buenos_aires",
    "name": {"de": "Buenos Aires", "en": "Buenos Aires"},
    "category": "hauptstaedte",
    "difficulty": 3,
    "facts": {"country": "Argentinien", "country_en": "Argentina", "continent": "Südamerika", "population_million": 3.1, "known_for": ["Tango", "La Boca", "Pampas", "Steak"], "language": "Spanisch"},
    "hints": [
      {"de": "Es ist die Hauptstadt von Argentinien", "en": "It is the capital of Argentina"},
      {"de": "Der Tango wurde hier erfunden", "en": "The Tango was invented here"},
      {"de": "Es wird manchmal 'Paris Südamerikas' genannt", "en": "It is sometimes called 'the Paris of South America'"}
    ],
    "description": {"de": "Buenos Aires ist die Hauptstadt Argentiniens und das kulturelle Zentrum Südamerikas. Der Tango wurde hier geboren. Die Stadt hat eine stark europäisch geprägte Architektur.", "en": "Buenos Aires is the capital of Argentina and the cultural center of South America. The Tango was born here. The city has a strongly European-influenced architecture."},
    "fun_fact": {"de": "Buenos Aires hat mehr Psychotherapeuten pro Einwohner als jede andere Stadt der Welt! Argentinien ist weltweit bekannt für seine Therapie-Kultur — sogar Kinder gehen regelmäßig zum Therapeuten.", "en": "Buenos Aires has more psychotherapists per capita than any other city in the world! Argentina is internationally known for its therapy culture — even children regularly see therapists."},
    "flag_url": "https://flagcdn.com/w320/ar.png",
    "emoji": "🇦🇷",
    "qa_context": "Buenos Aires, Hauptstadt Argentinien, 3,1 Mio. Einwohner (15 Mio. Großraum), Südamerika, Spanisch, bekannt für Tango (Erfindungsort), La Boca, europäische Architektur, Paris Südamerikas genannt, Steak"
  },
  {
    "id": "seoul",
    "name": {"de": "Seoul", "en": "Seoul"},
    "category": "hauptstaedte",
    "difficulty": 3,
    "facts": {"country": "Südkorea", "country_en": "South Korea", "continent": "Asien", "population_million": 10, "known_for": ["K-Pop", "Samsung/Hyundai", "Palast Gyeongbokgung", "schnellstes Internet der Welt"], "language": "Koreanisch"},
    "hints": [
      {"de": "Es ist die Hauptstadt von Südkorea", "en": "It is the capital of South Korea"},
      {"de": "K-Pop und Hallyu (Korean Wave) kommen von hier", "en": "K-Pop and Hallyu (Korean Wave) come from here"},
      {"de": "Es hat das schnellste Internet der Welt", "en": "It has the world's fastest internet"}
    ],
    "description": {"de": "Seoul ist die Hauptstadt Südkoreas mit 10 Millionen Einwohnern. K-Pop, K-Drama und Samsung sind von hier. Die Stadt verbindet alte Königspaläste mit ultramoderner Technologie.", "en": "Seoul is the capital of South Korea with 10 million inhabitants. K-Pop, K-Drama and Samsung originate here. The city combines ancient royal palaces with ultra-modern technology."},
    "fun_fact": {"de": "Seoul hat das schnellste Internet der Welt und mehr öffentliches WLAN als fast jede andere Stadt! K-Pop-Stars wie BTS und BLACKPINK machen Südkorea zu einem globalen Kulturexporteur.", "en": "Seoul has the world's fastest internet and more public WiFi than almost any other city! K-Pop stars like BTS and BLACKPINK make South Korea a global cultural exporter."},
    "flag_url": "https://flagcdn.com/w320/kr.png",
    "emoji": "🇰🇷",
    "qa_context": "Seoul, Hauptstadt Südkorea, 10 Mio. Einwohner, Asien, Koreanisch, bekannt für K-Pop, BTS, Samsung, Hyundai, schnellstes Internet, Palast Gyeongbokgung, Kimchi, Han-Fluss"
  },
  {
    "id": "ottawa_new",
    "id": "reykjavik",
    "name": {"de": "Reykjavík", "en": "Reykjavik"},
    "category": "hauptstaedte",
    "difficulty": 3,
    "facts": {"country": "Island", "country_en": "Iceland", "continent": "Europa", "population_million": 0.13, "known_for": ["Nordlichter", "Geysire", "Mitternachtssonne", "Björk"], "language": "Isländisch"},
    "hints": [
      {"de": "Es ist die Hauptstadt von Island", "en": "It is the capital of Iceland"},
      {"de": "Es ist die nördlichste Hauptstadt der Welt", "en": "It is the northernmost capital in the world"},
      {"de": "Man kann hier Nordlichter sehen", "en": "You can see the Northern Lights here"}
    ],
    "description": {"de": "Reykjavík ist die Hauptstadt Islands und die nördlichste Hauptstadt der Welt. Die Stadt liegt auf einer Vulkaninsel und nutzt Geothermie für fast 100% ihrer Energie. Nordlichter sind hier zu sehen.", "en": "Reykjavik is the capital of Iceland and the northernmost capital in the world. The city sits on a volcanic island and uses geothermal energy for almost 100% of its energy. Northern lights can be seen here."},
    "fun_fact": {"de": "Island hat fast keine Kriminalität — Reykjavík gilt als eine der sichersten Hauptstädte der Welt. Außerdem haben alle Isländer keinen Familiennamen: Der Nachname ist immer 'Vorname des Vaters + son/dóttir'.", "en": "Iceland has almost no crime — Reykjavik is one of the world's safest capitals. Also, all Icelanders have no family name: the last name is always 'father's first name + son/dóttir'."},
    "flag_url": "https://flagcdn.com/w320/is.png",
    "emoji": "🇮🇸",
    "qa_context": "Reykjavík, Reykjavik, Hauptstadt Island, 130.000 Einwohner, nördlichste Hauptstadt der Welt, Nordatlantik, Europa, Isländisch, bekannt für Nordlichter, Geysire, Geothermie, Vulkane, Mitternachtssonne, sicherste Stadt der Welt"
  }
]

# ─── TIERE (new items) ────────────────────────────────────────────────────────
new_tiere = [
  {
    "id": "pferd",
    "name": {"de": "Pferd", "en": "Horse"},
    "category": "tiere",
    "difficulty": 1,
    "facts": {"type": "Säugetier", "habitat": "Wiesen und Weiden", "diet": "Pflanzenfresser", "size_cm": 150, "legs": 4, "speed_kmh": 70, "domestic": True},
    "hints": [
      {"de": "Es ist ein großes Haustier mit vier Beinen", "en": "It is a large pet with four legs"},
      {"de": "Menschen reiten darauf", "en": "Humans ride on it"},
      {"de": "Es kann sehr schnell laufen und galoppieren", "en": "It can run very fast and gallop"}
    ],
    "description": {"de": "Das Pferd ist eines der ältesten Haustiere des Menschen. Jahrhundertelang half es bei der Arbeit, im Krieg und als Transportmittel. Heute werden Pferde vor allem zum Reiten gehalten.", "en": "The horse is one of humanity's oldest domestic animals. For centuries it helped with work, in war and as transportation. Today horses are kept mainly for riding."},
    "fun_fact": {"de": "Pferde können fast 360 Grad sehen — nur direkt vor ihrer Nase und hinter dem Schwanz haben sie einen blinden Fleck! Außerdem schlafen sie im Stehen, weil Aufstehen für sie viel Kraft kostet.", "en": "Horses can see almost 360 degrees — only directly in front of their nose and behind their tail do they have a blind spot! Also, they sleep standing up because getting up requires a lot of effort for them."},
    "emoji": "🐴",
    "qa_context": "Pferd, Hengst, Stute, Fohlen, Haustier, Säugetier, 4 Beine, Pflanzenfresser, Gras, Wiese, reiten, galoppieren, traben, Hufe, Mähne, Schwanz, bis 70 km/h schnell, schlafen stehend"
  },
  {
    "id": "schwein",
    "name": {"de": "Schwein", "en": "Pig"},
    "category": "tiere",
    "difficulty": 1,
    "facts": {"type": "Säugetier", "habitat": "Bauernhof", "diet": "Allesfresser", "size_cm": 90, "legs": 4, "domestic": True, "sound": "Grunzen"},
    "hints": [
      {"de": "Es lebt auf dem Bauernhof", "en": "It lives on the farm"},
      {"de": "Es macht Grunzgeräusche", "en": "It makes grunting sounds"},
      {"de": "Es wälzt sich gerne im Schlamm, um sich abzukühlen", "en": "It loves to roll in mud to cool down"}
    ],
    "description": {"de": "Das Schwein ist eines der am häufigsten gehaltenen Nutztiere der Welt. Schweine sind sehr intelligent — sogar intelligenter als Hunde! Sie wälzen sich im Schlamm, weil sie nicht schwitzen können.", "en": "The pig is one of the most commonly kept farm animals in the world. Pigs are very intelligent — even smarter than dogs! They roll in mud because they cannot sweat."},
    "fun_fact": {"de": "Schweine sind klüger als Hunde und können sogar Videospiele spielen! In Versuchen lernten Schweine, mit einer Spielkonsole umzugehen. Außerdem können sie keinen Sonnenbrand bekommen — nein, warten: Sie KÖNNEN Sonnenbrand bekommen, deshalb brauchen sie den Schlamm!", "en": "Pigs are smarter than dogs and can even play video games! In experiments, pigs learned to operate a game console. Also, they CAN get sunburned — that's exactly why they need the mud!"},
    "emoji": "🐷",
    "qa_context": "Schwein, Ferkel, Sau, Eber, Bauernhof, Säugetier, 4 Beine, Allesfresser, Schlamm wälzen, Grunzen, rosa, Rüssel, Ringelschwanz, sehr intelligent, klüger als Hunde, Haustier/Nutztier"
  },
  {
    "id": "kuh",
    "name": {"de": "Kuh", "en": "Cow"},
    "category": "tiere",
    "difficulty": 1,
    "facts": {"type": "Säugetier", "habitat": "Wiesen und Bauernhöfe", "diet": "Pflanzenfresser", "size_cm": 140, "legs": 4, "domestic": True, "sound": "Muhen"},
    "hints": [
      {"de": "Es lebt auf der Weide und gibt uns Milch", "en": "It lives in the meadow and gives us milk"},
      {"de": "Es macht 'Muh'", "en": "It says 'moo'"},
      {"de": "Es hat vier Mägen", "en": "It has four stomachs"}
    ],
    "description": {"de": "Die Kuh ist das wichtigste Nutztier für Milch weltweit. Sie verbringt fast 8 Stunden täglich mit Fressen und kaut ihr Futter mehrmals wieder (Wiederkäuer). Sie hat 4 Mägen.", "en": "The cow is the most important dairy animal worldwide. It spends almost 8 hours a day eating and chews its food multiple times (ruminant). It has 4 stomachs."},
    "fun_fact": {"de": "Kühe haben beste Freunde! Untersuchungen zeigen, dass Kühe, die mit ihrer besten Freundin zusammen sind, weniger Stress haben und mehr Milch geben. Sie können ihre Freundin an der Stimme erkennen.", "en": "Cows have best friends! Studies show that cows with their best friend nearby have less stress and produce more milk. They can recognize their friend by their voice."},
    "emoji": "🐮",
    "qa_context": "Kuh, Rind, Kalb, Stier, Bulle, Bauernhof, Weide, Säugetier, 4 Beine, Pflanzenfresser, Gras, Milch, Muhen, schwarz-weiß oder braun, 4 Mägen, Wiederkäuer, Hörner"
  },
  {
    "id": "schaf",
    "name": {"de": "Schaf", "en": "Sheep"},
    "category": "tiere",
    "difficulty": 1,
    "facts": {"type": "Säugetier", "habitat": "Wiesen und Berge", "diet": "Pflanzenfresser", "size_cm": 75, "legs": 4, "domestic": True, "sound": "Blöken"},
    "hints": [
      {"de": "Es hat eine dicke Wollschicht und wird geschoren", "en": "It has a thick wool coat and is sheared"},
      {"de": "Es blökt und lebt in Herden", "en": "It bleats and lives in herds"},
      {"de": "Aus seiner Wolle wird Kleidung gemacht", "en": "Its wool is made into clothing"}
    ],
    "description": {"de": "Das Schaf ist eines der ältesten Haustiere. Seine Wolle wird zu Kleidung, Teppichen und Decken verarbeitet. Schafe leben in Herden und folgen einander — daher der Begriff 'Herdentier'.", "en": "The sheep is one of the oldest domestic animals. Its wool is processed into clothing, carpets and blankets. Sheep live in herds and follow each other — hence the term 'herd animal'."},
    "fun_fact": {"de": "Schafe können sich bis zu 50 Gesichter von anderen Schafen über 2 Jahre lang merken! Sie haben auch ein gutes Gedächtnis für Orte, wo sie gutes Futter gefunden haben. Das macht sie klüger als ihr Ruf.", "en": "Sheep can remember up to 50 faces of other sheep for over 2 years! They also have good memory for places where they found good food. This makes them smarter than their reputation suggests."},
    "emoji": "🐑",
    "qa_context": "Schaf, Lamm, Widder, Wolle, Blöken, Bauernhof, Wiese, Säugetier, 4 Beine, Pflanzenfresser, Herde, Herdentier, weiß, geschoren, Wolle für Kleidung, Berge"
  },
  {
    "id": "huhn",
    "name": {"de": "Huhn", "en": "Chicken"},
    "category": "tiere",
    "difficulty": 1,
    "facts": {"type": "Vogel", "habitat": "Bauernhof", "diet": "Allesfresser", "legs": 2, "domestic": True, "sound": "Gackern", "lays_eggs": True},
    "hints": [
      {"de": "Es ist ein Vogel, der auf dem Bauernhof lebt", "en": "It is a bird that lives on the farm"},
      {"de": "Es legt Eier, die wir essen", "en": "It lays eggs that we eat"},
      {"de": "Es gackert und flattert, kann aber kaum fliegen", "en": "It clucks and flutters but can barely fly"}
    ],
    "description": {"de": "Das Huhn ist das häufigste Haustier der Welt — es gibt mehr Hühner als Menschen! Es legt Eier und sein Fleisch wird weltweit gegessen. Hühner können kaum fliegen.", "en": "The chicken is the world's most common domestic animal — there are more chickens than humans! It lays eggs and its meat is eaten worldwide. Chickens can barely fly."},
    "fun_fact": {"de": "Es gibt mehr Hühner als Menschen auf der Erde! Ca. 33 Milliarden Hühner stehen 8 Milliarden Menschen gegenüber. Ein Huhn legt im Jahr ca. 250-300 Eier — fast jeden Tag eines!", "en": "There are more chickens than humans on Earth! About 33 billion chickens compare to 8 billion humans. A chicken lays about 250-300 eggs per year — almost one every day!"},
    "emoji": "🐔",
    "qa_context": "Huhn, Henne, Hahn, Küken, Vogel, Bauernhof, Eier legen, gackern, krähen (Hahn), Federn, Flügel, kaum fliegen können, weiß/braun/bunt, Allesfresser, meistgehaltenes Haustier der Welt"
  },
  {
    "id": "fuchs",
    "name": {"de": "Fuchs", "en": "Fox"},
    "category": "tiere",
    "difficulty": 2,
    "facts": {"type": "Säugetier", "habitat": "Wälder und Städte", "diet": "Allesfresser", "size_cm": 70, "legs": 4, "domestic": False},
    "hints": [
      {"de": "Es ist ein schlaues Wildtier mit rotem Fell", "en": "It is a clever wild animal with red fur"},
      {"de": "Es lebt im Wald, aber auch in Städten", "en": "It lives in forests but also in cities"},
      {"de": "Es ist bekannt aus Märchen als listiges Tier", "en": "It is known from fairy tales as a cunning animal"}
    ],
    "description": {"de": "Der Fuchs ist ein anpassungsfähiges Wildtier, das in Wäldern, aber auch in Städten lebt. Er ist bekannt für seine Schlauheit und sein rotes Fell. In Märchen ist er oft der listige Trickster.", "en": "The fox is an adaptable wild animal that lives in forests but also in cities. It is known for its cleverness and red fur. In fairy tales it is often the cunning trickster."},
    "fun_fact": {"de": "Füchse nutzen das Erdmagnetfeld zur Jagd! Wenn ein Fuchs auf eine Maus zuläuft, springt er fast immer aus nordöstlicher Richtung — weil er so am genauesten trifft. Das wurde von Wissenschaftlern untersucht.", "en": "Foxes use Earth's magnetic field for hunting! When a fox runs at a mouse, it almost always jumps from the northeast — because it's most accurate this way. This was studied by scientists."},
    "emoji": "🦊",
    "qa_context": "Fuchs, rotes Fell, Wildtier, Wald, Städte, Säugetier, 4 Beine, Allesfresser, schlau/listig, Märchen, buschiger Schwanz, Fuchsbau, nachtaktiv, Mäuse fressen"
  },
  {
    "id": "wolf",
    "name": {"de": "Wolf", "en": "Wolf"},
    "category": "tiere",
    "difficulty": 2,
    "facts": {"type": "Säugetier", "habitat": "Wälder und Gebirge", "diet": "Fleischfresser", "size_cm": 80, "legs": 4, "domestic": False, "pack_animal": True},
    "hints": [
      {"de": "Es ist der Vorfahre des Haushundes", "en": "It is the ancestor of the domestic dog"},
      {"de": "Es lebt in Rudeln und heult", "en": "It lives in packs and howls"},
      {"de": "Es ist seit Jahren nach Deutschland zurückgekehrt", "en": "It has returned to Germany in recent years"}
    ],
    "description": {"de": "Der Wolf ist der wilde Vorfahre aller Haushunde. Er lebt in Rudeln und kommuniziert durch Heulen. Nach langer Abwesenheit sind Wölfe in den letzten Jahrzehnten nach Deutschland zurückgekehrt.", "en": "The wolf is the wild ancestor of all domestic dogs. It lives in packs and communicates by howling. After a long absence, wolves have returned to Germany in recent decades."},
    "fun_fact": {"de": "Der Haushund und der Wolf sind so eng verwandt, dass sie sich kreuzen können — ihre Jungtiere sind fruchtbar! DNA-Analysen zeigen: Alle Hunde der Welt, vom Chihuahua bis zur Dogge, stammen vom Wolf ab.", "en": "The domestic dog and the wolf are so closely related that they can interbreed — their offspring are fertile! DNA analyses show: all dogs in the world, from Chihuahua to Great Dane, are descended from the wolf."},
    "emoji": "🐺",
    "qa_context": "Wolf, Wölfin, Welpen, Rudel, Heulen, Wald, Gebirge, Säugetier, 4 Beine, Fleischfresser, Vorfahre des Hundes, Deutschland (zurückgekehrt), grau/weiß, Märchen (böser Wolf)"
  },
  {
    "id": "biene",
    "name": {"de": "Biene", "en": "Bee"},
    "category": "tiere",
    "difficulty": 2,
    "facts": {"type": "Insekt", "habitat": "Wiesen und Gärten", "diet": "Pflanzenfresser (Nektar, Pollen)", "size_cm": 1.5, "legs": 6, "wings": 4, "domestic": False},
    "hints": [
      {"de": "Es ist ein kleines geflügeltes Insekt, das Honig macht", "en": "It is a small winged insect that makes honey"},
      {"de": "Es lebt in Völkern mit einer Königin", "en": "It lives in colonies with a queen"},
      {"de": "Es ist sehr wichtig für die Bestäubung von Pflanzen", "en": "It is very important for pollinating plants"}
    ],
    "description": {"de": "Die Biene ist eines der wichtigsten Tiere für unser Ökosystem. Sie bestäubt Pflanzen und produziert Honig. Eine Bienenkönigin kann bis zu 5 Jahre leben und legt bis zu 2.000 Eier pro Tag.", "en": "The bee is one of the most important animals for our ecosystem. It pollinates plants and produces honey. A queen bee can live up to 5 years and lays up to 2,000 eggs per day."},
    "fun_fact": {"de": "Eine Arbeitsbiene produziert in ihrem ganzen Leben nur einen Teelöffel Honig! Für ein Glas Honig (500g) muss eine Biene etwa 40.000 km fliegen — einmal um die Erde.", "en": "A worker bee produces only one teaspoon of honey in its entire life! For one jar of honey (500g), a bee must fly about 40,000 km — once around the Earth."},
    "emoji": "🐝",
    "qa_context": "Biene, Honigbiene, Hummel, Insekt, 6 Beine, 4 Flügel, Honig, Nektar, Blüten bestäuben, Bienenvolk, Königin, Arbeiterinnen, Drohnen, stechen, sehr wichtig für Ökosystem"
  },
  {
    "id": "adler",
    "name": {"de": "Adler", "en": "Eagle"},
    "category": "tiere",
    "difficulty": 2,
    "facts": {"type": "Vogel", "habitat": "Berge und Wälder", "diet": "Fleischfresser", "wingspan_cm": 200, "legs": 2, "can_fly": True},
    "hints": [
      {"de": "Es ist ein großer Greifvogel mit scharfen Augen", "en": "It is a large bird of prey with sharp eyes"},
      {"de": "Es kann sehr hoch fliegen und sehr weit sehen", "en": "It can fly very high and see very far"},
      {"de": "Es ist das nationale Symbol vieler Länder, auch Deutschlands", "en": "It is the national symbol of many countries, including Germany"}
    ],
    "description": {"de": "Der Adler ist einer der größten und stärksten Greifvögel. Er sieht fünfmal schärfer als Menschen. Der Adler ist Symbol von Stärke und Freiheit und erscheint im deutschen Wappen.", "en": "The eagle is one of the largest and strongest birds of prey. It sees five times more sharply than humans. The eagle is a symbol of strength and freedom and appears in the German coat of arms."},
    "fun_fact": {"de": "Adler können ihre Beute aus bis zu 3 km Entfernung sehen! Wenn Menschen so scharf sehen könnten, könnten wir von einem Hochhaus aus eine Ameise auf dem Boden erkennen.", "en": "Eagles can spot their prey from up to 3 km away! If humans could see that sharply, we could spot an ant on the ground from the top of a skyscraper."},
    "emoji": "🦅",
    "qa_context": "Adler, Seeadler, Steinadler, Greifvogel, Vogel, 2 Beine, Flügel, sehr scharfe Augen, Fleischfresser, Berge, hoch fliegen, deutsches Wappen, Symbol für Stärke und Freiheit, Horst (Nest)"
  },
  {
    "id": "krokodil",
    "name": {"de": "Krokodil", "en": "Crocodile"},
    "category": "tiere",
    "difficulty": 2,
    "facts": {"type": "Reptil", "habitat": "Tropische Flüsse und Sümpfe", "diet": "Fleischfresser", "size_cm": 400, "legs": 4, "domestic": False, "lifespan_years": 70},
    "hints": [
      {"de": "Es ist ein großes Reptil, das im Wasser und an Land lebt", "en": "It is a large reptile that lives in water and on land"},
      {"de": "Es hat ein Maul mit vielen scharfen Zähnen", "en": "It has a jaw with many sharp teeth"},
      {"de": "Es lebte schon zur Zeit der Dinosaurier", "en": "It already lived in the time of the dinosaurs"}
    ],
    "description": {"de": "Das Krokodil ist eines der ältesten Lebewesen der Erde — es hat die Dinosaurier überlebt! Es lebt in tropischen Flüssen und Sümpfen. Ein Krokodil kann über 70 Jahre alt werden.", "en": "The crocodile is one of Earth's oldest creatures — it survived the dinosaurs! It lives in tropical rivers and swamps. A crocodile can live over 70 years."},
    "fun_fact": {"de": "Krokodile können nicht kauen! Sie reißen Fleisch ab und schlucken es in großen Stücken. Außerdem produzieren sie keine echten Tränen aus Trauer — aber Krokodilstränen beim Fressen sind tatsächlich real, weil Fressen die Tränendrüsen stimuliert.", "en": "Crocodiles cannot chew! They tear off flesh and swallow it in large pieces. Also, they don't produce real tears from sadness — but crocodile tears while eating are actually real, because eating stimulates the tear glands."},
    "emoji": "🐊",
    "qa_context": "Krokodil, Alligator, Reptil, 4 Beine, Fleischfresser, tropisch, Flüsse, Sümpfe, Afrika, Asien, Amerika, scharfe Zähne, sehr alte Tierart (Dinosaurierzeit), bis 70 Jahre alt, grün/braun, Schuppen"
  },
  {
    "id": "oktopus",
    "name": {"de": "Oktopus", "en": "Octopus"},
    "category": "tiere",
    "difficulty": 3,
    "facts": {"type": "Weichtier", "habitat": "Meere weltweit", "diet": "Fleischfresser", "arms": 8, "legs": 0, "domestic": False, "hearts": 3},
    "hints": [
      {"de": "Es lebt im Meer und hat 8 Arme", "en": "It lives in the sea and has 8 arms"},
      {"de": "Es kann seine Farbe und Form blitzschnell ändern", "en": "It can change its color and shape instantly"},
      {"de": "Es hat 3 Herzen und blaues Blut", "en": "It has 3 hearts and blue blood"}
    ],
    "description": {"de": "Der Oktopus ist eines der intelligentesten Tiere im Meer. Er hat 8 Arme mit Saugnäpfen, kann seine Farbe ändern und Tinte spritzen. Er hat 3 Herzen und blaues Blut.", "en": "The octopus is one of the most intelligent animals in the sea. It has 8 arms with suckers, can change color and squirt ink. It has 3 hearts and blue blood."},
    "fun_fact": {"de": "Oktopusse haben 3 Herzen — zwei pumpen Blut durch die Kiemen, eines durch den Körper. Ihr Blut ist blau, weil es Kupfer statt Eisen enthält! Und wenn sie schwimmen, hört das Hauptherz auf zu schlagen.", "en": "Octopuses have 3 hearts — two pump blood through the gills, one through the body. Their blood is blue because it contains copper instead of iron! And when they swim, the main heart stops beating."},
    "emoji": "🐙",
    "qa_context": "Oktopus, Tintenfisch, Meerestier, 8 Arme, Saugnäpfe, Meer/Ozean, Fleischfresser, Tinte spritzen, Farbe wechseln, 3 Herzen, blaues Blut, sehr intelligent, keine Knochen, Weichtier"
  },
  {
    "id": "pinguin",
    "name": {"de": "Pinguin", "en": "Penguin"},
    "category": "tiere",
    "difficulty": 2,
    "facts": {"type": "Vogel", "habitat": "Antarktis und Südamerika", "diet": "Fleischfresser (Fisch)", "size_cm": 100, "legs": 2, "can_fly": False, "can_swim": True},
    "hints": [
      {"de": "Es ist ein Vogel, der nicht fliegen, aber sehr gut schwimmen kann", "en": "It is a bird that cannot fly but can swim very well"},
      {"de": "Es trägt ein schwarz-weißes 'Frack'-Muster", "en": "It wears a black and white 'tuxedo' pattern"},
      {"de": "Es lebt meist in sehr kalten Regionen", "en": "It mostly lives in very cold regions"}
    ],
    "description": {"de": "Der Pinguin ist ein Vogel, der nicht fliegen kann, dafür aber ein exzellenter Schwimmer ist. Die meisten Pinguine leben in der Antarktis. Sie haben ein schwarz-weißes Gefieder wie ein Smoking.", "en": "The penguin is a bird that cannot fly but is an excellent swimmer. Most penguins live in Antarctica. They have black and white plumage like a tuxedo."},
    "fun_fact": {"de": "Pinguinmännchen machen ihrer Partnerin einen Heiratsantrag mit einem besonderen Kieselstein! Wenn ein Männchen einen schönen Stein findet, legt er ihn der Auserwählten zu Füßen. Wenn sie ihn nimmt, sind sie ein Paar.", "en": "Male penguins propose to their mate with a special pebble! When a male finds a beautiful stone, he places it at his chosen one's feet. If she takes it, they are a couple."},
    "emoji": "🐧",
    "qa_context": "Pinguin, Vogel, schwimmen (nicht fliegen), Antarktis, Südamerika, schwarz-weiß, Fisch essen, Kälte, Eis, Kolonien, Küken, watscheln"
  },
  {
    "id": "fledermaus",
    "name": {"de": "Fledermaus", "en": "Bat"},
    "category": "tiere",
    "difficulty": 3,
    "facts": {"type": "Säugetier", "habitat": "Höhlen, Dachböden, Wälder", "diet": "Insekten (meist)", "legs": 2, "wings": 2, "can_fly": True, "nocturnal": True},
    "hints": [
      {"de": "Es ist das einzige Säugetier, das wirklich fliegen kann", "en": "It is the only mammal that can truly fly"},
      {"de": "Es ist nachtaktiv und schläft kopfüber hängend", "en": "It is nocturnal and sleeps hanging upside down"},
      {"de": "Es findet sich mit Ultraschall zurecht", "en": "It navigates using ultrasound"}
    ],
    "description": {"de": "Die Fledermaus ist das einzige fliegende Säugetier. Sie ist nachtaktiv und orientiert sich durch Echolokation (Ultraschall). Fledermäuse fressen enorme Mengen Insekten und sind wichtig für das Ökosystem.", "en": "The bat is the only truly flying mammal. It is nocturnal and navigates through echolocation (ultrasound). Bats eat enormous amounts of insects and are important for the ecosystem."},
    "fun_fact": {"de": "Eine einzige Fledermaus kann in einer Nacht bis zu 1.000 Mücken fressen! Sie sind natürliche Insektizide. Ohne Fledermäuse würden Insekten sich unkontrolliert vermehren und Ernten zerstören.", "en": "A single bat can eat up to 1,000 mosquitoes in one night! They are natural insecticides. Without bats, insects would multiply uncontrollably and destroy crops."},
    "emoji": "🦇",
    "qa_context": "Fledermaus, Säugetier, einziges fliegendes Säugetier, nachtaktiv, Ultraschall/Echolokation, Höhlen, Dachböden, kopfüber schlafen, Insekten fressen, kein schlechtes Sehen (Augen funktionieren!), Halloween-Symbol"
  },
  {
    "id": "hai",
    "name": {"de": "Hai", "en": "Shark"},
    "category": "tiere",
    "difficulty": 2,
    "facts": {"type": "Fisch", "habitat": "Meere weltweit", "diet": "Fleischfresser", "size_cm": 600, "legs": 0, "fins": True},
    "hints": [
      {"de": "Es ist ein großer Fisch im Meer mit scharfen Zähnen", "en": "It is a large fish in the sea with sharp teeth"},
      {"de": "Es hat eine dreieckige Rückenflosse", "en": "It has a triangular dorsal fin"},
      {"de": "Es muss ständig schwimmen, um zu atmen", "en": "It must constantly swim to breathe"}
    ],
    "description": {"de": "Der Hai ist einer der ältesten Fische der Erde — er existiert seit 450 Millionen Jahren. Er hat keine Knochen (nur Knorpel) und muss ständig schwimmen, damit Wasser durch seine Kiemen fließt.", "en": "The shark is one of Earth's oldest fish — it has existed for 450 million years. It has no bones (only cartilage) and must constantly swim so water flows through its gills."},
    "fun_fact": {"de": "Haie töten jährlich nur ca. 10 Menschen weltweit. Menschen töten aber jährlich über 100 Millionen Haie! Außerdem leuchten manche Haie im Dunkeln — das wurde erst vor wenigen Jahren entdeckt.", "en": "Sharks kill only about 10 people worldwide per year. But humans kill over 100 million sharks annually! Also, some sharks glow in the dark — this was only discovered a few years ago."},
    "emoji": "🦈",
    "qa_context": "Hai, Weißer Hai, Hammerhai, Walhai, Fisch, Meer/Ozean, Fleischfresser, scharfe Zähne, Flossen, keine Knochen (Knorpel), muss schwimmen zum Atmen, sehr alte Tierart (450 Mio. Jahre)"
  },
  {
    "id": "koalabear",
    "name": {"de": "Koala", "en": "Koala"},
    "category": "tiere",
    "difficulty": 3,
    "facts": {"type": "Beuteltier", "habitat": "Australien", "diet": "Eukalyptus-Blätter", "size_cm": 70, "legs": 4, "domestic": False, "sleep_hours": 22},
    "hints": [
      {"de": "Es kommt aus Australien und sieht aus wie ein kleiner Bär", "en": "It comes from Australia and looks like a small bear"},
      {"de": "Es schläft fast 22 Stunden pro Tag", "en": "It sleeps almost 22 hours per day"},
      {"de": "Es frisst fast nur Eukalyptus-Blätter", "en": "It eats almost only eucalyptus leaves"}
    ],
    "description": {"de": "Der Koala ist ein Beuteltier aus Australien, kein Bär. Er schläft bis zu 22 Stunden täglich, weil Eukalyptusblätter wenig Energie liefern und sogar giftig für andere Tiere sind. Koalas haben einzigartige Fingerabdrücke wie Menschen.", "en": "The koala is a marsupial from Australia, not a bear. It sleeps up to 22 hours daily because eucalyptus leaves provide little energy and are even toxic to other animals. Koalas have unique fingerprints like humans."},
    "fun_fact": {"de": "Koalas haben Fingerabdrücke, die denen von Menschen so ähnlich sind, dass sie Spurensicherungsexperten schon verwirrt haben! Sogar unter dem Mikroskop sind sie kaum von menschlichen Fingerabdrücken zu unterscheiden.", "en": "Koalas have fingerprints so similar to human ones that they've confused forensic experts! Even under a microscope they are barely distinguishable from human fingerprints."},
    "emoji": "🐨",
    "qa_context": "Koala, Koalabär (kein echter Bär!), Beuteltier, Australien, Eukalyptus fressen, bis 22 Stunden schlafen, grau, Klettern, Beutel (Jungtiere), einzigartige Fingerabdrücke"
  }
]

# ─── GEMÜSE (new items) ───────────────────────────────────────────────────────
new_gemuese = [
  {
    "id": "brokkoli",
    "name": {"de": "Brokkoli", "en": "Broccoli"},
    "category": "gemuese",
    "difficulty": 1,
    "facts": {"color": "grün", "type": "Kreuzblütler", "edible_part": "Blütenkopf und Stiel", "origin": "Mittelmeer", "vitamin_c": "sehr hoch"},
    "hints": [
      {"de": "Es ist grünes Gemüse, das wie ein kleiner Baum aussieht", "en": "It is green vegetable that looks like a small tree"},
      {"de": "Kinder mögen es oft nicht, obwohl es sehr gesund ist", "en": "Children often dislike it, although it is very healthy"},
      {"de": "Es stammt aus der Kohlpflanzenfamilie", "en": "It comes from the cabbage plant family"}
    ],
    "description": {"de": "Brokkoli ist ein grünes Gemüse aus der Kohlfamilie. Es ist sehr reich an Vitamin C und K. Brokkoli stammt ursprünglich aus dem Mittelmeerraum und wird weltweit gegessen.", "en": "Broccoli is a green vegetable from the cabbage family. It is very rich in vitamin C and K. Broccoli originally comes from the Mediterranean and is eaten worldwide."},
    "fun_fact": {"de": "Brokkoli enthält mehr Vitamin C als Orangen! 100g Brokkoli liefern fast doppelt so viel Vitamin C wie 100g Orange. Außerdem ist er mit Blumenkohl so nah verwandt, dass Wissenschaftler Brokkoli mit weißem Blumenkohl kreuzen konnten.", "en": "Broccoli contains more vitamin C than oranges! 100g of broccoli provides almost twice as much vitamin C as 100g of orange. Also, it's so closely related to cauliflower that scientists were able to cross broccoli with white cauliflower."},
    "emoji": "🥦",
    "qa_context": "Brokkoli, grünes Gemüse, sieht wie Baum aus, Kohlgewächs, sehr gesund, Vitamin C, roh oder gekocht, Stiel und Röschen, Mittelmeer, häufig bei Kindern unbeliebt"
  },
  {
    "id": "blumenkohl",
    "name": {"de": "Blumenkohl", "en": "Cauliflower"},
    "category": "gemuese",
    "difficulty": 1,
    "facts": {"color": "weiß", "type": "Kreuzblütler", "edible_part": "Blütenstand", "origin": "Mittelmeer"},
    "hints": [
      {"de": "Es ist weißes Gemüse, das wie eine Wolke aussieht", "en": "It is white vegetable that looks like a cloud"},
      {"de": "Es ist eng mit Brokkoli verwandt, aber weiß statt grün", "en": "It is closely related to broccoli but white instead of green"},
      {"de": "Man kann es zu Pizza-Boden oder Reis verarbeiten", "en": "It can be processed into pizza base or rice"}
    ],
    "description": {"de": "Blumenkohl ist ein weißes Gemüse aus der Kohlfamilie. Er ist sehr vielseitig: Er kann als Gemüsebeilage, als Suppe oder sogar als glutenfreier Pizza-Boden verwendet werden.", "en": "Cauliflower is a white vegetable from the cabbage family. It is very versatile: it can be used as a vegetable side dish, as soup or even as a gluten-free pizza base."},
    "fun_fact": {"de": "Blumenkohl ist eigentlich ein riesiger Haufen von Blüten, die nie aufgeblüht sind! Was wir essen, heißt 'Quark' oder 'Curd' — Tausende kleiner Blütenknospen, die kompakt zusammengewachsen sind.", "en": "Cauliflower is actually a huge bunch of flowers that never bloomed! What we eat is called 'curd' — thousands of tiny flower buds that grew together compactly."},
    "emoji": "🥦",
    "qa_context": "Blumenkohl, Karfiol, weiß, wie Wolke aussehen, Kohlfamilie, Kreuzblütler, gesund, roh oder gekocht, Pizza-Boden, Blütenstand, Mittelmeer"
  },
  {
    "id": "erbse",
    "name": {"de": "Erbse", "en": "Pea"},
    "category": "gemuese",
    "difficulty": 1,
    "facts": {"color": "grün", "type": "Hülsenfrüchte", "edible_part": "Samen", "protein": "hoch"},
    "hints": [
      {"de": "Es ist ein kleines, rundes, grünes Gemüse", "en": "It is a small, round, green vegetable"},
      {"de": "Es wächst in einer Schote und wird roh oder gekocht gegessen", "en": "It grows in a pod and is eaten raw or cooked"},
      {"de": "Es ist für das Märchen 'Prinzessin auf der Erbse' bekannt", "en": "It is known from the fairy tale 'The Princess and the Pea'"}
    ],
    "description": {"de": "Erbsen sind kleine, runde, grüne Hülsenfrüchte. Sie wachsen in einer Schote und sind reich an Proteinen und Vitaminen. Erbsen können roh als Snack oder gekocht als Beilage gegessen werden.", "en": "Peas are small, round, green legumes. They grow in a pod and are rich in proteins and vitamins. Peas can be eaten raw as a snack or cooked as a side dish."},
    "fun_fact": {"de": "Gregor Mendel entdeckte die Gesetze der Vererbung — also warum Kinder ihren Eltern ähneln — durch Experimente mit Erbsen! Er kreuzte über 10.000 Erbsenpflanzen und entdeckte dabei die Grundlagen der modernen Genetik.", "en": "Gregor Mendel discovered the laws of heredity — why children resemble their parents — through experiments with peas! He crossed over 10,000 pea plants and discovered the foundations of modern genetics."},
    "emoji": "🫛",
    "qa_context": "Erbse, Schote, grün, rund, klein, Hülsenfrucht, Protein, tiefgefroren oder frisch, Mendel (Genetik), Märchen Prinzessin auf der Erbse, roh oder gekocht"
  },
  {
    "id": "spinat",
    "name": {"de": "Spinat", "en": "Spinach"},
    "category": "gemuese",
    "difficulty": 1,
    "facts": {"color": "grün", "type": "Blattgemüse", "edible_part": "Blätter", "origin": "Persien", "iron": "hoch"},
    "hints": [
      {"de": "Es ist ein grünes Blattgemüse, bekannt aus dem Popeye-Cartoon", "en": "It is a green leafy vegetable, known from the Popeye cartoon"},
      {"de": "Es macht angeblich stark, weil es viel Eisen enthält", "en": "It supposedly makes you strong because it contains lots of iron"},
      {"de": "Es kann roh als Salat oder gekocht gegessen werden", "en": "It can be eaten raw as salad or cooked"}
    ],
    "description": {"de": "Spinat ist ein grünes Blattgemüse aus Persien. Er ist reich an Eisen, Vitaminen und Mineralien. Durch den Cartoon-Seemann Popeye wurde Spinat als Symbol für Kraft berühmt.", "en": "Spinach is a green leafy vegetable from Persia. It is rich in iron, vitamins and minerals. Through the cartoon sailor Popeye, spinach became famous as a symbol of strength."},
    "fun_fact": {"de": "Der Eisengehalt von Spinat wurde im 19. Jahrhundert irrtümlich um das Zehnfache überschätzt! Ein Wissenschaftler setzte ein Komma falsch. Der Mythos 'Spinat ist super-eisenreich' blieb — und inspirierte sogar Popeye.", "en": "The iron content of spinach was mistakenly overestimated tenfold in the 19th century! A scientist put a decimal point in the wrong place. The myth 'spinach is super iron-rich' remained — and even inspired Popeye."},
    "emoji": "🥬",
    "qa_context": "Spinat, grünes Blattgemüse, Eisen, Popeye, stark machen, Persien, roh oder gekocht, Blattsalat, Smoothie, Babyspinat"
  },
  {
    "id": "lauch",
    "name": {"de": "Lauch", "en": "Leek"},
    "category": "gemuese",
    "difficulty": 2,
    "facts": {"color": "grün/weiß", "type": "Lauchgewächs", "edible_part": "Stängel und Blätter", "origin": "Mittelmeer"},
    "hints": [
      {"de": "Es ist ein stängelförmiges Gemüse, weiß unten und grün oben", "en": "It is a stem-shaped vegetable, white at the bottom and green at the top"},
      {"de": "Es schmeckt wie eine milde Zwiebel", "en": "It tastes like a mild onion"},
      {"de": "Es ist das Nationalgemüse von Wales", "en": "It is the national vegetable of Wales"}
    ],
    "description": {"de": "Lauch (Porree) ist ein Zwiebelgewächs mit mildem Geschmack. Er ist weiß am Stängel und grün an den Blättern. Lauch ist reich an Vitaminen und wird in Suppen, Eintöpfen und als Beilage verwendet.", "en": "Leek is a member of the onion family with a mild flavor. It is white at the stem and green at the leaves. Leek is rich in vitamins and used in soups, stews and as a side dish."},
    "fun_fact": {"de": "Lauch ist das Nationalgemüse von Wales! Walisische Soldaten sollen im 7. Jahrhundert Lauchpflanzen an ihren Helmen getragen haben, um sich im Kampf von Feinden zu unterscheiden. Heute ist der Lauch im walisischen Wappen.", "en": "Leek is the national vegetable of Wales! Welsh soldiers reportedly wore leek plants on their helmets in the 7th century to distinguish themselves from enemies in battle. Today the leek is in the Welsh coat of arms."},
    "emoji": "🧄",
    "qa_context": "Lauch, Porree, Stange, weiß und grün, Zwiebelgewächs, milder Geschmack, Suppe, Wales (Nationalgemüse), Lauchsuppe, Quiche"
  },
  {
    "id": "spargel",
    "name": {"de": "Spargel", "en": "Asparagus"},
    "category": "gemuese",
    "difficulty": 2,
    "facts": {"color": "weiß oder grün", "type": "Spargelgewächs", "edible_part": "Triebe", "season": "April-Juni"},
    "hints": [
      {"de": "Es ist ein stängelförmiges Gemüse, das im Frühjahr geerntet wird", "en": "It is a stem-shaped vegetable harvested in spring"},
      {"de": "Es ist weiß oder grün und kommt aus der Erde", "en": "It is white or green and comes from the ground"},
      {"de": "In Deutschland wird es 'König der Gemüse' genannt und besonders gefeiert", "en": "In Germany it is called 'King of Vegetables' and especially celebrated"}
    ],
    "description": {"de": "Spargel ist ein Frühlingsgemüse, das nur von April bis Juni geerntet wird. In Deutschland ist er besonders beliebt — die Spargelsaison ist ein kulinarisches Ereignis. Weißer Spargel wächst unter der Erde.", "en": "Asparagus is a spring vegetable harvested only from April to June. It is especially popular in Germany — asparagus season is a culinary event. White asparagus grows underground."},
    "fun_fact": {"de": "Weißer und grüner Spargel sind exakt die gleiche Pflanze! Weißer Spargel wächst abgedeckt ohne Licht (kein Chlorophyll = keine grüne Farbe). Sobald er Sonnenlicht bekommt, wird er grün.", "en": "White and green asparagus are exactly the same plant! White asparagus grows covered without light (no chlorophyll = no green color). As soon as it gets sunlight, it turns green."},
    "emoji": "🌿",
    "qa_context": "Spargel, weiß oder grün, Frühjahr, April-Juni, König der Gemüse, Deutschland, aus der Erde, Stangen, Spargelsuppe, König der Gemüse"
  },
  {
    "id": "rote_bete",
    "name": {"de": "Rote Bete", "en": "Beetroot"},
    "category": "gemuese",
    "difficulty": 2,
    "facts": {"color": "dunkelrot", "type": "Rübengewächs", "edible_part": "Knolle", "betain": True},
    "hints": [
      {"de": "Es ist ein dunkelrotes, rundes Gemüse", "en": "It is a dark red, round vegetable"},
      {"de": "Es färbt beim Kochen alles, was es berührt, tief rot", "en": "It dyes everything it touches deep red when cooking"},
      {"de": "Es schmeckt leicht erdig und süßlich", "en": "It tastes slightly earthy and sweet"}
    ],
    "description": {"de": "Rote Bete ist eine dunkelrote Rübe mit einem erdigen, leicht süßlichen Geschmack. Sie ist sehr reich an Folsäure und Eisen. Sie wird roh, gekocht oder eingelegt gegessen.", "en": "Beetroot is a dark red root vegetable with an earthy, slightly sweet taste. It is very rich in folic acid and iron. It is eaten raw, cooked or pickled."},
    "fun_fact": {"de": "Rote Bete färbt den Urin rot — das ist vollkommen harmlos und normal! Trotzdem erschrecken sich viele Menschen, wenn das passiert. Der Farbstoff Betain ist der Grund und sogar ein natürlicher Lebensmittelfarbstoff.", "en": "Beetroot turns urine red — this is completely harmless and normal! Still, many people are startled when this happens. The pigment betanin is the reason and is even a natural food dye."},
    "emoji": "🫚",
    "qa_context": "Rote Bete, Rübe, dunkelrot, färbt alles rot, rund, erdig-süß, Folsäure, Eisen, roh oder gekocht, eingelegt, Salat, Saft"
  },
  {
    "id": "sellerie",
    "name": {"de": "Sellerie", "en": "Celery"},
    "category": "gemuese",
    "difficulty": 2,
    "facts": {"color": "hellgrün/weiß", "type": "Doldenblütler", "edible_part": "Stiel oder Knolle", "calories": "sehr niedrig"},
    "hints": [
      {"de": "Es ist ein Gemüse mit sehr knackigem Stiel oder runder Knolle", "en": "It is a vegetable with a very crunchy stalk or round bulb"},
      {"de": "Es hat einen starken, charakteristischen Geruch", "en": "It has a strong, characteristic smell"},
      {"de": "Es ist eines der kalorienärmsten Gemüse überhaupt", "en": "It is one of the lowest-calorie vegetables of all"}
    ],
    "description": {"de": "Sellerie gibt es als Staudensellerie (grüne Stängel) und Knollensellerie (weiße Knolle). Er hat einen intensiven Geschmack und Geruch und ist sehr kalorienarm. Er wird roh, gekocht oder als Suppe gegessen.", "en": "Celery comes as stalk celery (green stems) and celeriac (white bulb). It has an intense taste and smell and is very low in calories. It is eaten raw, cooked or as soup."},
    "fun_fact": {"de": "Sellerie hat so wenige Kalorien, dass man beim Kauen fast genauso viele verbrennt wie man aufnimmt! 100g Staudensellerie haben nur 14 Kalorien. Daher gilt er als 'Null-Kalorien-Lebensmittel' (obwohl das nicht ganz stimmt).", "en": "Celery has so few calories that you burn almost as many chewing as you take in! 100g of stalk celery has only 14 calories. Hence it is considered a 'zero-calorie food' (although that's not quite right)."},
    "emoji": "🥬",
    "qa_context": "Sellerie, Staudensellerie, Knollensellerie, hellgrün, weißliche Knolle, starker Geruch, kalorienarm, Suppe (Suppenkraut), roh oder gekocht, knackig"
  },
  {
    "id": "artischocke",
    "name": {"de": "Artischocke", "en": "Artichoke"},
    "category": "gemuese",
    "difficulty": 3,
    "facts": {"color": "grün/violett", "type": "Korbblütler", "edible_part": "Blütenböden und Blattbasen", "origin": "Mittelmeer"},
    "hints": [
      {"de": "Es ist ein Gemüse, das wie eine geschlossene Blume aussieht", "en": "It is a vegetable that looks like a closed flower"},
      {"de": "Man zieht die Blätter heraus und tunkt sie in Soße", "en": "You pull out the leaves and dip them in sauce"},
      {"de": "Nur der Boden und das Innere der Blätter sind essbar", "en": "Only the base and the inside of the leaves are edible"}
    ],
    "description": {"de": "Die Artischocke ist die essbare Blütenknospe einer Distelart. Man isst den Boden (Artischockenboden) und den Fleischanteil der Blätter. Sie ist reich an Ballaststoffen und Antioxidantien.", "en": "The artichoke is the edible flower bud of a thistle species. You eat the base (artichoke heart) and the meaty part of the leaves. It is rich in fiber and antioxidants."},
    "fun_fact": {"de": "Was wir 'Artischockenherz' nennen, ist eigentlich gar kein Herz — es ist der Boden der Blütenknospe! Echter Artischockenboden ist so wertvoll, dass er oft in teuren Restaurants serviert wird. Außerdem macht Artischocke Wasser süß, wenn man danach trinkt.", "en": "What we call 'artichoke heart' is not actually a heart — it's the base of the flower bud! The true artichoke bottom is so valuable it's often served in expensive restaurants. Also, artichoke makes water taste sweet if you drink after eating it."},
    "emoji": "🥦",
    "qa_context": "Artischocke, Blütenknospe, Distel, grün oder violett, Mittelmeer, Blätter abzupfen, Artischockenboden/-herz, reich an Ballaststoffen, mediterrane Küche"
  },
  {
    "id": "fenchel",
    "name": {"de": "Fenchel", "en": "Fennel"},
    "category": "gemuese",
    "difficulty": 3,
    "facts": {"color": "grün/weiß", "type": "Doldenblütler", "taste": "Anis-ähnlich", "edible_part": "Knolle, Stiel und Blätter", "origin": "Mittelmeer"},
    "hints": [
      {"de": "Es ist ein Gemüse mit Anis-Geschmack", "en": "It is a vegetable with an anise flavor"},
      {"de": "Es hat eine weiße Knolle und grüne, fedrige Blätter", "en": "It has a white bulb and green, feathery leaves"},
      {"de": "Es wird auch als Verdauungsmittel oder Tee verwendet", "en": "It is also used as a digestive aid or tea"}
    ],
    "description": {"de": "Fenchel hat einen charakteristischen Anis-Geschmack. Die weiße Knolle wird als Gemüse gegessen, die Samen als Gewürz. Fenchelltee hilft gegen Bauchweh — Eltern geben ihn oft Babys.", "en": "Fennel has a characteristic anise flavor. The white bulb is eaten as a vegetable, the seeds as a spice. Fennel tea helps with stomach aches — parents often give it to babies."},
    "fun_fact": {"de": "Fenchel ist eines der ältesten Heilmittel der Menschheit! Im antiken Griechenland wurde Fenchel als Wunderpflanze verehrt: Er sollte Mut geben, Gewicht reduzieren und sogar das Sehvermögen verbessern. Das Wort 'Marathon' kommt möglicherweise vom griechischen Wort für Fenchel.", "en": "Fennel is one of humanity's oldest medicines! In ancient Greece, fennel was revered as a miracle plant: it was said to give courage, reduce weight and even improve eyesight. The word 'Marathon' may come from the Greek word for fennel."},
    "emoji": "🌿",
    "qa_context": "Fenchel, Anis-Geschmack, weiße Knolle, grüne Blätter, Tee, Heilpflanze, Mittelmeer, Bauch, Samen als Gewürz, mediterrane Küche"
  },
  {
    "id": "zucchini",
    "name": {"de": "Zucchini", "en": "Zucchini"},
    "category": "gemuese",
    "difficulty": 2,
    "facts": {"color": "grün (meist)", "type": "Kürbisgewächs", "edible_part": "Frucht", "origin": "Amerika/Italien"},
    "hints": [
      {"de": "Es ist ein längliches, grünes Gemüse aus der Kürbisfamilie", "en": "It is an elongated, green vegetable from the squash family"},
      {"de": "Es kann gebraten, gedünstet oder roh gegessen werden", "en": "It can be fried, steamed or eaten raw"},
      {"de": "Man kann es zu Spaghetti formen ('Zoodles')", "en": "It can be spiralized into noodles ('Zoodles')"}
    ],
    "description": {"de": "Zucchini ist ein Sommergemüse aus der Kürbisfamilie. Sie ist sehr vielseitig: roh, gebraten, gebacken oder als 'Zoodles' (Zucchini-Spaghetti). Sie enthält viel Wasser und ist sehr kalorienarm.", "en": "Zucchini is a summer vegetable from the squash family. It is very versatile: raw, fried, baked or as 'zoodles' (zucchini spaghetti). It contains lots of water and is very low in calories."},
    "fun_fact": {"de": "Eine Zucchini-Pflanze kann in einem Sommer so viele Früchte produzieren, dass Gärtner sie heimlich in Autos von Nachbarn werfen — weil sie nicht mehr wissen, wohin damit! In den USA ist das ein echter Brauch am 'National Sneak Some Zucchini Onto Your Neighbor's Porch Day'.", "en": "A zucchini plant can produce so many fruits in one summer that gardeners secretly throw them into neighbors' cars — because they don't know what to do with them all! In the US this is a real custom on 'National Sneak Some Zucchini Onto Your Neighbor's Porch Day'."},
    "emoji": "🥒",
    "qa_context": "Zucchini, Zucchetto, grün, länglich, Kürbisgewächs, Sommer, kalorienarm, Wasser, braten, dünsten, Zoodles (Nudeln), roh oder gekocht, vielseitig"
  },
  {
    "id": "rosenkohl",
    "name": {"de": "Rosenkohl", "en": "Brussels Sprouts"},
    "category": "gemuese",
    "difficulty": 2,
    "facts": {"color": "grün", "type": "Kreuzblütler", "edible_part": "Knospen", "origin": "Belgien", "season": "Herbst/Winter"},
    "hints": [
      {"de": "Es sind kleine, runde, grüne Kügelchen, die wie Miniatur-Kohlköpfe aussehen", "en": "They are small, round, green balls that look like miniature cabbages"},
      {"de": "Viele Kinder mögen es nicht — es hat einen starken Geschmack", "en": "Many children don't like it — it has a strong flavor"},
      {"de": "Es kommt ursprünglich aus Belgien", "en": "It originally comes from Belgium"}
    ],
    "description": {"de": "Rosenkohl sind kleine, grüne Kohlköpfchen, die an einem langen Stiel wachsen. Sie sind reich an Vitamin C und K. Der starke Geruch beim Kochen macht sie bei Kindern unbeliebt.", "en": "Brussels sprouts are small, green cabbage heads that grow on a long stalk. They are rich in vitamin C and K. The strong smell when cooking makes them unpopular with children."},
    "fun_fact": {"de": "Rosenkohl wurde ursprünglich in Belgien (nahe Brüssel) gezüchtet — daher der Name 'Brussels Sprouts'! Außerdem kann man ihn in den meisten deutschen Gärten noch nach dem ersten Frost ernten: Frost macht ihn sogar süßer.", "en": "Brussels sprouts were originally cultivated in Belgium (near Brussels) — hence the name 'Brussels Sprouts'! Also, you can harvest them in most German gardens even after the first frost: frost actually makes them sweeter."},
    "emoji": "🥦",
    "qa_context": "Rosenkohl, Brüsseler Kohl, kleine Kohlköpfchen, grün, rund, Belgien, Herbst/Winter, Vitamin C, starker Geruch, bei Kindern unbeliebt, am Stiel wachsend"
  }
]

# ─── OBST (new items) ──────────────────────────────────────────────────────────
new_obst = [
  {
    "id": "pflaume",
    "name": {"de": "Pflaume", "en": "Plum"},
    "category": "obst",
    "difficulty": 1,
    "facts": {"color": "blau/lila", "type": "Steinobst", "origin": "Asien", "pit": True, "season": "Sommer/Herbst"},
    "hints": [
      {"de": "Es ist ein blau-lila Steinobst", "en": "It is a blue-purple stone fruit"},
      {"de": "Es wächst an Bäumen und hat einen Kern in der Mitte", "en": "It grows on trees and has a pit in the middle"},
      {"de": "Getrocknet heißt es Backpflaume oder Dörrpflaume", "en": "When dried it is called a prune"}
    ],
    "description": {"de": "Die Pflaume ist ein Steinobst mit blau-lila Schale und gelbem Fruchtfleisch. Sie wird frisch, als Kompott, Marmelade oder Pflaumenkuchen gegessen. Getrocknet heißt sie Dörrpflaume.", "en": "The plum is a stone fruit with blue-purple skin and yellow flesh. It is eaten fresh, as compote, jam or plum cake. When dried it is called a prune."},
    "fun_fact": {"de": "Pflaumenbäume können über 100 Jahre alt werden und noch immer Früchte tragen! In manchen deutschen Dörfern gibt es Pflaumenbäume, die noch aus dem 19. Jahrhundert stammen und die Bewohner noch immer mit Früchten versorgen.", "en": "Plum trees can live over 100 years and still bear fruit! In some German villages there are plum trees dating from the 19th century that still supply residents with fruit."},
    "emoji": "🫐",
    "qa_context": "Pflaume, Zwetschge, blau-lila, Steinobst, Kern/Stein, Baum, Sommer, Pflaumenkuchen, Kompott, Marmelade, getrocknet = Dörrpflaume"
  },
  {
    "id": "weintraube",
    "name": {"de": "Weintraube", "en": "Grape"},
    "category": "obst",
    "difficulty": 1,
    "facts": {"color": "grün oder lila", "type": "Beerenobst", "origin": "Naher Osten", "grows_on": "Weinreben", "used_for": ["Wein", "Rosinen", "Saft"]},
    "hints": [
      {"de": "Es ist ein kleines, rundes Obst, das in Trauben wächst", "en": "It is a small, round fruit that grows in bunches"},
      {"de": "Es gibt es in grün und lila und es kann zu Wein verarbeitet werden", "en": "It comes in green and purple and can be made into wine"},
      {"de": "Getrocknet heißt es Rosine", "en": "When dried it is called a raisin"}
    ],
    "description": {"de": "Weintrauben wachsen in Trauben an Weinreben. Sie gibt es grün und lila. Trauben werden frisch gegessen oder zu Wein, Saft und Rosinen verarbeitet. Der Anbau von Weintrauben heißt Weinbau.", "en": "Grapes grow in bunches on vines. They come in green and purple. Grapes are eaten fresh or processed into wine, juice and raisins. Cultivating grapes is called viticulture."},
    "fun_fact": {"de": "Weintrauben gibt es seit mindestens 8.000 Jahren! Die älteste bekannte Weinkelter wurde in Armenien gefunden und ist 6.100 Jahre alt. Heute gibt es über 10.000 verschiedene Traubensorten weltweit.", "en": "Grapes have existed for at least 8,000 years! The oldest known winery was found in Armenia and is 6,100 years old. Today there are over 10,000 different grape varieties worldwide."},
    "emoji": "🍇",
    "qa_context": "Weintraube, Traube, grün oder lila/rot, Weinrebe, Beerenobst, Wein, Rosinen, Saft, in Trauben wachsend, rund, klein, süß oder sauer"
  },
  {
    "id": "kirsche",
    "name": {"de": "Kirsche", "en": "Cherry"},
    "category": "obst",
    "difficulty": 1,
    "facts": {"color": "rot oder schwarz", "type": "Steinobst", "pit": True, "season": "Juni/Juli", "origin": "Europa/Asien"},
    "hints": [
      {"de": "Es ist ein kleines, rotes Obst mit einem Stein", "en": "It is a small, red fruit with a pit"},
      {"de": "Es wird im Frühsommer geerntet", "en": "It is harvested in early summer"},
      {"de": "Der Schwarzwälder Kirschtorte ist nach ihm benannt", "en": "The Black Forest cake is named after it"}
    ],
    "description": {"de": "Kirschen sind kleine Steinfrüchte, meist rot oder dunkelrot. Sie werden im Juni und Juli geerntet. Sie werden frisch gegessen, zu Marmelade, Saft oder Kuchen verarbeitet.", "en": "Cherries are small stone fruits, usually red or dark red. They are harvested in June and July. They are eaten fresh, processed into jam, juice or cake."},
    "fun_fact": {"de": "Es gibt eine Kirschenkernspuckweltmeisterschaft! In Langenlois (Österreich) wird jährlich der 'Kirschkernweitwurf' ausgetragen. Der Rekord liegt bei über 20 Metern! Die Technik ist wichtig: kein Pusten, sondern Spucken mit der Zunge.", "en": "There is a cherry pit spitting world championship! In Langenlois (Austria), the 'cherry pit spitting' competition is held annually. The record is over 20 meters! Technique matters: not blowing but spitting with the tongue."},
    "emoji": "🍒",
    "qa_context": "Kirsche, rot oder schwarz, Steinobst, klein, Stein/Kern, Sommer (Juni/Juli), Baumobst, Schwarzwälder Kirschtorte, Marmelade, Saft, Weichsel, Sauerkirsche"
  },
  {
    "id": "grapefruit",
    "name": {"de": "Grapefruit", "en": "Grapefruit"},
    "category": "obst",
    "difficulty": 2,
    "facts": {"color": "gelb-rosa", "type": "Zitrusfrucht", "taste": "bitter-sauer", "origin": "Karibik", "vitamin_c": "hoch"},
    "hints": [
      {"de": "Es ist eine große Zitrusfrucht, die bitter-sauer schmeckt", "en": "It is a large citrus fruit that tastes bitter-sour"},
      {"de": "Es ist eine natürliche Kreuzung aus Orange und Pampelmuse", "en": "It is a natural cross between orange and pomelo"},
      {"de": "Es kann mit manchen Medikamenten gefährlich reagieren", "en": "It can dangerously interact with some medications"}
    ],
    "description": {"de": "Die Grapefruit ist eine Zitrusfrucht mit gelber Schale und rosa-gelbem Fruchtfleisch. Sie schmeckt bitter-sauer und enthält viel Vitamin C. Sie ist eine natürliche Kreuzung aus Orange und Pampelmuse.", "en": "The grapefruit is a citrus fruit with yellow skin and pink-yellow flesh. It tastes bitter-sour and contains lots of vitamin C. It is a natural cross between orange and pomelo."},
    "fun_fact": {"de": "Grapefruit kann die Wirkung von über 85 Medikamenten verändern — und das ist kein Witz! Ein Stoff in der Grapefruit blockiert Enzyme in der Leber, die Medikamente abbauen. Dadurch kann die Medikamentendosis im Blut auf das Vierfache ansteigen.", "en": "Grapefruit can change the effect of over 85 medications — and that's no joke! A substance in grapefruit blocks enzymes in the liver that break down medications. This can cause medication levels in the blood to rise to four times the normal amount."},
    "emoji": "🍊",
    "qa_context": "Grapefruit, Pampelmuse, Zitrusfrucht, gelb-rosa, bitter-sauer, groß, Vitamin C, Karibik, Kreuzung Orange/Pampelmuse, Medikamentenwechselwirkung"
  },
  {
    "id": "feige",
    "name": {"de": "Feige", "en": "Fig"},
    "category": "obst",
    "difficulty": 2,
    "facts": {"color": "lila/grün", "type": "Beerenobst", "origin": "Naher Osten", "sweet": True, "dried": True},
    "hints": [
      {"de": "Es ist ein birnenförmiges, lila Obst mit süßem Innenleben", "en": "It is a pear-shaped, purple fruit with a sweet interior"},
      {"de": "Es ist eines der ältesten kultivierten Früchte der Menschheit", "en": "It is one of the oldest cultivated fruits of humanity"},
      {"de": "Getrocknete Version ist ein beliebter Weihnachtssnack", "en": "The dried version is a popular Christmas snack"}
    ],
    "description": {"de": "Die Feige ist eine der ältesten Kulturpflanzen der Menschheit — sie wird seit mindestens 11.000 Jahren angebaut. Sie hat ein weiches, süßes Fruchtfleisch mit vielen kleinen Samen.", "en": "The fig is one of humanity's oldest cultivated plants — it has been grown for at least 11,000 years. It has a soft, sweet flesh with many small seeds."},
    "fun_fact": {"de": "Eine Feige ist eigentlich kein Obst im botanischen Sinne — es ist eine umgestülpte Blüte! Die kleinen Samen im Inneren sind die eigentlichen Früchte. Außerdem können manche Feigen nur durch eine ganz spezifische Wespenart bestäubt werden.", "en": "A fig is not actually a fruit in the botanical sense — it is an inverted flower! The small seeds inside are the actual fruits. Also, some figs can only be pollinated by one very specific wasp species."},
    "emoji": "🫐",
    "qa_context": "Feige, lila oder grün, süß, innen rot/rosa, viele kleine Samen, getrocknet, Naher Osten, Mittelmeer, sehr alte Kulturpflanze, Feigenbaum, Weihnachten"
  },
  {
    "id": "himbeere",
    "name": {"de": "Himbeere", "en": "Raspberry"},
    "category": "obst",
    "difficulty": 1,
    "facts": {"color": "rot", "type": "Beerenobst", "origin": "Europa/Asien", "season": "Sommer"},
    "hints": [
      {"de": "Es ist eine kleine, rote Beere, die aus vielen kleinen Kügelchen besteht", "en": "It is a small, red berry made up of many small droplets"},
      {"de": "Es wächst an dornigen Sträuchern", "en": "It grows on thorny bushes"},
      {"de": "Es ist für Marmelade, Smoothies und Eis sehr beliebt", "en": "It is very popular for jam, smoothies and ice cream"}
    ],
    "description": {"de": "Die Himbeere ist eine kleine rote Beere, die aus vielen kleinen Steinfrüchtchen besteht. Sie wächst an stacheligen Sträuchern und wird im Sommer geerntet. Sie ist sehr beliebt für Marmelade und Eis.", "en": "The raspberry is a small red berry made up of many tiny drupelets. It grows on thorny bushes and is harvested in summer. It is very popular for jam and ice cream."},
    "fun_fact": {"de": "Eine Himbeere ist eigentlich keine einzelne Frucht! Sie besteht aus bis zu 100 kleinen Einzelfrüchtchen, jedes mit einem eigenen Kern. Die hohle Mitte entsteht, weil die Himbeere beim Pflücken von der Scheinbeere getrennt wird.", "en": "A raspberry is actually not a single fruit! It consists of up to 100 small individual drupelets, each with its own seed. The hollow center forms because the raspberry separates from the receptacle when picked."},
    "emoji": "🍓",
    "qa_context": "Himbeere, rot, Beere, Beerenobst, viele kleine Kügelchen/Drüpchen, Dornenstrauch, Sommer, Marmelade, Smoothie, Eis, Parfüm-Aroma"
  },
  {
    "id": "johannisbeere",
    "name": {"de": "Johannisbeere", "en": "Currant"},
    "category": "obst",
    "difficulty": 2,
    "facts": {"color": "rot, schwarz oder weiß", "type": "Beerenobst", "origin": "Europa", "season": "Sommer"},
    "hints": [
      {"de": "Es ist eine kleine Beere, die in Trauben wächst — rot, schwarz oder weiß", "en": "It is a small berry that grows in clusters — red, black or white"},
      {"de": "Sie ist sehr sauer und wird meist zu Saft oder Marmelade verarbeitet", "en": "It is very sour and usually processed into juice or jam"},
      {"de": "Schwarze Johannisbeeren haben besonders viel Vitamin C", "en": "Black currants have particularly high vitamin C"}
    ],
    "description": {"de": "Johannisbeeren sind kleine, saure Beeren in Trauben. Es gibt sie rot, schwarz oder weiß. Schwarze Johannisbeeren haben dreimal so viel Vitamin C wie Orangen. Sie werden zu Saft, Gelee oder Marmelade verarbeitet.", "en": "Currants are small, sour berries in clusters. They come in red, black or white. Black currants have three times more vitamin C than oranges. They are processed into juice, jelly or jam."},
    "fun_fact": {"de": "Schwarze Johannisbeeren sind vitamin-C-Weltmeister unter den heimischen Früchten! 100g schwarze Johannisbeeren enthalten 180mg Vitamin C — fast viermal so viel wie Orangen. Daher sind sie trotz ihres sauren Geschmacks sehr wertvoll.", "en": "Black currants are vitamin C world champions among native fruits! 100g of black currants contain 180mg of vitamin C — almost four times as much as oranges. Hence they are very valuable despite their sour taste."},
    "emoji": "🍇",
    "qa_context": "Johannisbeere, Ribisel (österreichisch), rot oder schwarz oder weiß, kleine Beere, Trauben, sauer, Vitamin C, Sommer, Saft, Gelee, Marmelade, Strauch"
  },
  {
    "id": "granatapfel",
    "name": {"de": "Granatapfel", "en": "Pomegranate"},
    "category": "obst",
    "difficulty": 3,
    "facts": {"color": "rot (außen und Kerne)", "type": "Kernobst", "origin": "Persien/Naher Osten", "seeds_count": 600, "antioxidants": "sehr hoch"},
    "hints": [
      {"de": "Es ist ein rundes, rotes Obst, das innen hunderte kleine rubinrote Kerne enthält", "en": "It is a round, red fruit containing hundreds of tiny ruby-red seeds inside"},
      {"de": "Es ist in der Bibel und im Koran erwähnt", "en": "It is mentioned in the Bible and the Quran"},
      {"de": "Es ist das Symbol für Fruchtbarkeit in vielen Kulturen", "en": "It is a symbol of fertility in many cultures"}
    ],
    "description": {"de": "Der Granatapfel ist eine uralte Frucht aus dem Nahen Osten. Im Inneren befinden sich hunderte rubinrote Kerne (Arils), die man essen kann. Er ist reich an Antioxidantien.", "en": "The pomegranate is an ancient fruit from the Middle East. Inside are hundreds of ruby-red seeds (arils) that you can eat. It is rich in antioxidants."},
    "fun_fact": {"de": "Ein Granatapfel enthält durchschnittlich 613 Kerne — und in manchen Kulturen gibt es den Brauch, sie alle zu zählen! In Griechenland wird an Neujahr ein Granatapfel auf den Boden geworfen: Je mehr Kerne herausfallen, desto mehr Glück im neuen Jahr.", "en": "A pomegranate contains on average 613 seeds — and in some cultures there is the custom of counting them all! In Greece, a pomegranate is thrown on the floor at New Year: the more seeds that fall out, the more luck in the new year."},
    "emoji": "🍎",
    "qa_context": "Granatapfel, Pomegranate, rot, rund, viele kleine Kerne/Samen (Arils), rubinrot, Naher Osten, Persien, sehr alt, Antioxidantien, Symbol Fruchtbarkeit, Neujahr (Griechenland)"
  },
  {
    "id": "papaya",
    "name": {"de": "Papaya", "en": "Papaya"},
    "category": "obst",
    "difficulty": 3,
    "facts": {"color": "orange (Fruchtfleisch)", "type": "Exotische Frucht", "origin": "Mittelamerika", "enzyme": "Papain"},
    "hints": [
      {"de": "Es ist ein tropisches Obst mit orangefarbenem Fruchtfleisch und schwarzen Kernen", "en": "It is a tropical fruit with orange flesh and black seeds"},
      {"de": "Es kommt aus Mittelamerika und wächst an einem hohen Baum", "en": "It comes from Central America and grows on a tall tree"},
      {"de": "Es enthält ein Enzym, das Fleisch mürbe macht", "en": "It contains an enzyme that tenderizes meat"}
    ],
    "description": {"de": "Die Papaya ist eine tropische Frucht mit süßem, orangem Fruchtfleisch und schwarzen Kernen. Sie enthält das Enzym Papain, das Eiweiß abbaut und daher zum Zartmachen von Fleisch verwendet wird.", "en": "The papaya is a tropical fruit with sweet, orange flesh and black seeds. It contains the enzyme papain, which breaks down protein and is therefore used to tenderize meat."},
    "fun_fact": {"de": "Das Enzym Papain in Papayas ist so stark, dass man Fleisch darin einlegen kann, um es zart zu machen — das haben Ureinwohner Mittelamerikas seit Jahrtausenden gemacht! Papain wird auch in Waschmittel und Fleischzartmachern verwendet.", "en": "The enzyme papain in papayas is so powerful that you can marinate meat in it to tenderize it — Indigenous peoples of Central America have done this for millennia! Papain is also used in laundry detergent and meat tenderizers."},
    "emoji": "🍈",
    "qa_context": "Papaya, tropisch, orange Fruchtfleisch, schwarze Kerne, Mittelamerika, süß, groß, Papain (Enzym), Fleisch mürbe machen, warm, exotisch"
  }
]

def merge_data(filepath, new_items):
    with open(filepath, 'r', encoding='utf-8') as f:
        existing = json.load(f)
    existing_ids = {item['id'] for item in existing}
    added = 0
    for item in new_items:
        if item.get('id') and item['id'] not in existing_ids:
            existing.append(item)
            existing_ids.add(item['id'])
            added += 1
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    return len(existing), added

# Fix duplicate id issue in new_hauptstaedte
seen = set()
deduped = []
for item in new_hauptstaedte:
    if item.get('id') and item['id'] not in seen:
        seen.add(item['id'])
        deduped.append(item)
new_hauptstaedte = deduped

total, added = merge_data(os.path.join(DATA, 'hauptstaedte.json'), new_hauptstaedte)
print(f"hauptstaedte: {total} total (+{added})")

total, added = merge_data(os.path.join(DATA, 'tiere.json'), new_tiere)
print(f"tiere: {total} total (+{added})")

total, added = merge_data(os.path.join(DATA, 'gemuese.json'), new_gemuese)
print(f"gemuese: {total} total (+{added})")

total, added = merge_data(os.path.join(DATA, 'obst.json'), new_obst)
print(f"obst: {total} total (+{added})")

print("\nDone!")
