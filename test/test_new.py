from service.handler import Handler




mass = [["Коровы", "нюрка"], ["Собаки", "Шарик"]]


Handler.add_table(mass, file_name="Приказ_о_заявлении_для_налоговой", rows=2, cols=2)







f = {"file_name":{
        "context": {},
        "tables": {
            1:{"size":100000,
                   "context":[]},
            2:{"size":50000,
                   "context":[]}
        },
        "meta_data": {}
    }
}
