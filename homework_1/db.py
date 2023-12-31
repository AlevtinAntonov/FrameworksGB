from datetime import date, timedelta

page_title = [' Задание 7', 'страница с блоками новостей']

news_1 = {'page_title': page_title,
          'news': 'Новость 1',
          'image': '/static/image/img2.jpg',
          'date_public': (date.today() - timedelta(3)).strftime("%d.%m.%Y"),
          'txt': "Имеется спорная точка зрения, гласящая примерно следующее: предприниматели в сети интернет "
                 "представляют собой не что иное, как квинтэссенцию победы маркетинга над разумом и должны быть "
                 "рассмотрены исключительно в разрезе маркетинговых и финансовых предпосылок! Имеется спорная точка "
                 "зрения, гласящая примерно следующее: элементы политического процесса могут быть заблокированы в "
                 "рамках своих собственных рациональных ограничений.", }

news_2 = {'page_title': page_title,
          'news': 'Новость 2',
          'image': '/static/image/img3.jpg',
          'date_public': (date.today() - timedelta(2)).strftime("%d.%m.%Y"),
          'txt': "Прежде всего, консультация с широким активом играет определяющее значение для кластеризации усилий. "
                 "Банальные, но неопровержимые выводы, а также сделанные на базе интернет-аналитики выводы лишь "
                 "добавляют фракционных разногласий и преданы социально-демократической анафеме.", }

news_3 = {'page_title': page_title,
          'news': 'Новость 3',
          'image': '/static/image/img4.jpg',
          'date_public': (date.today() - timedelta(1)).strftime("%d.%m.%Y"),
          'txt': "Господа, выбранный нами инновационный путь требует от нас анализа благоприятных перспектив. А также "
                 "многие известные личности набирают популярность среди определенных слоев населения, а значит, "
                 "должны быть представлены в исключительно положительном свете.", }

_news = [news_1, news_2, news_3]

_about = ["Учитывая ключевые сценарии поведения, граница обучения кадров напрямую зависит от новых принципов "
          "формирования материально-технической и кадровой базы. Вот вам яркий пример современных тенденций — "
          "высококачественный прототип будущего проекта напрямую зависит от соответствующих условий активизации. "
          "Ясность нашей позиции очевидна: существующая теория не оставляет шанса для своевременного выполнения "
          "сверхзадачи. Внезапно, сторонники тоталитаризма в науке набирают популярность среди определенных слоев "
          "населения, а значит, должны быть призваны к ответу.",
          "Равным образом, социально-экономическое развитие предоставляет широкие возможности для экспериментов, "
          "поражающих по своей масштабности и грандиозности! Приятно, граждане, наблюдать, как некоторые особенности "
          "внутренней политики являются только методом политического участия и указаны как претенденты на роль "
          "ключевых факторов. Противоположная точка зрения подразумевает, что базовые сценарии поведения "
          "пользователей представляют собой не что иное, как квинтэссенцию победы маркетинга над разумом и должны "
          "быть призваны к ответу. В своём стремлении повысить качество жизни, они забывают, что синтетическое "
          "тестирование требует определения и уточнения форм воздействия.",
          ]

_contacts = [{'name': 'Никанор',
              'mail': 'nik@mail.ru',
              'phone': '+7-987-654-32-10',
              },
             {'name': 'Феофан',
              'mail': 'feo@mail.ru',
              'phone': '+7-987-444-33-22',
              },
             {'name': 'Оверран',
              'mail': 'forest@mail.ru',
              'phone': '+7-903-333-33-33',
              }, ]

clothes_1 = {'item_title': 'Мужская одежда',
             'image': '/static/image/clothes_man.jpg',
             'txt': "В частности, выбранный нами инновационный путь прекрасно подходит для реализации распределения "
                    "внутренних резервов и ресурсов.", }
clothes_2 = {'item_title': 'Женская одежда',
             'image': '/static/image/clothes_woman.jpg',
             'txt': "Безусловно, повышение уровня гражданского сознания однозначно фиксирует необходимость "
                    "существующих финансовых и административных условий..", }
clothes_3 = {'item_title': 'Разная одежда',
             'image': '/static/image/clothes_people.jpg',
             'txt': "Как принято считать, предприниматели в сети интернет подвергнуты целой серии независимых "
                    "исследований.", }

_clothes = [clothes_1, clothes_2, clothes_3]


shoes_1 = {'item_title': 'Мужская обувь',
             'image': '/static/image/shoes_man.jpg',
             'txt': "Разнообразный и богатый опыт говорит нам, что экономическая повестка сегодняшнего дня "
                    "предоставляет широкие возможности для прогресса профессионального сообщества. Равным образом, "
                    "внедрение современных методик предоставляет широкие возможности для вывода текущих активов.", }
shoes_2 = {'item_title': 'Женская обувь',
             'image': '/static/image/shoes_women.jpg',
             'txt': "Мы вынуждены отталкиваться от того, что сплочённость команды профессионалов требует от нас "
                    "анализа стандартных подходов. Не следует, однако, забывать, что понимание сути "
                    "ресурсосберегающих технологий предопределяет высокую востребованность соответствующих условий "
                    "активизации.", }
shoes_3 = {'item_title': 'Детская обувь',
             'image': '/static/image/shoes_children.jpg',
             'txt': "Как уже неоднократно упомянуто, сторонники тоталитаризма в науке лишь добавляют фракционных "
                    "разногласий и подвергнуты целой серии независимых исследований. Не следует, однако, забывать, "
                    "что семантический разбор внешних противодействий позволяет выполнить важные задания по "
                    "разработке своевременного выполнения сверхзадачи.", }

_shoes = [shoes_1, shoes_2, shoes_3]


jackets_1 = {'item_title': 'Мужские куртки',
             'image': '/static/image/jacket_man.jpg',
             'txt': "А также непосредственные участники технического прогресса лишь добавляют фракционных разногласий "
                    "и преданы социально-демократической анафеме. Кстати, реплицированные с зарубежных источников, "
                    "современные исследования являются только методом политического участия и своевременно "
                    "верифицированы.", }
jackets_2 = {'item_title': 'Женские куртки',
             'image': '/static/image/jacket_women.jpeg',
             'txt': "Приятно, граждане, наблюдать, как представители современных социальных резервов лишь добавляют "
                    "фракционных разногласий и ассоциативно распределены по отраслям. Наше дело не так однозначно, "
                    "как может показаться: начало повседневной работы по формированию позиции играет определяющее "
                    "значение для глубокомысленных рассуждений.", }
jackets_3 = {'item_title': 'Разные куртки',
             'image': '/static/image/jacket_youth.jpg',
             'txt': "Равным образом, перспективное планирование, а также свежий взгляд на привычные вещи — безусловно "
                    "открывает новые горизонты для благоприятных перспектив. Приятно, граждане, наблюдать, "
                    "как независимые государства объединены в целые кластеры себе подобных.", }

_jackets = [jackets_1, jackets_2, jackets_3]
