links = pd.DataFrame([{"searches":25,"sourceCountry":"j","targetCountry":"n"},
                      {"searches":37,"sourceCountry":"o","targetCountry":"j"},
                      {"searches":16,"sourceCountry":"o","targetCountry":"l"},
                      {"searches":8,"sourceCountry":"o","targetCountry":"m"},
                      {"searches":68,"sourceCountry":"o","targetCountry":"k"},
                      {"searches":154,"sourceCountry":"g","targetCountry":"o"},
                      {"searches":40,"sourceCountry":"g","targetCountry":"i"},
                      {"searches":345,"sourceCountry":"b","targetCountry":"g"},
                      {"searches":66,"sourceCountry":"b","targetCountry":"h"},
                      {"searches":17,"sourceCountry":"b","targetCountry":"d"},
                      {"searches":25,"sourceCountry":"b","targetCountry":"e"},
                      {"searches":117,"sourceCountry":"b","targetCountry":"f"},
                      {"searches":692,"sourceCountry":"a","targetCountry":"b"},
                      {"searches":19,"sourceCountry":"a","targetCountry":"c"}])

sankey_chart = SankeyChart(links, 
                    source_column = 'sourceCountry', 
                    target_column = 'targetCountry', 
                    value_column ='searches', 
                    canvas_width=500, canvas_height=400)

sankey_chart.addLinkTooltip().show()