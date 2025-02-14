from service.handler import Handler




mass = [["Коровы", "нюрка"], ["Собаки", "Шарик"]]


Handler.add_table(mass, file_name="Приказ_о_заявлении_для_налоговой", rows=2, cols=2)







f = {
    "file_name":"Приказ_о_заявлении_для_налоговой",
    "context": {
        "name":"Иван",
        "DateRegistr":"27.01.2025", 
        "phone":"89011100011",
        "email":"easy@gamil.com",
        "ContractNumber":"111",
        "lastname":"иванов",
        "firstname":"Иван",
        "surname":"Иваныч",
        "DateOfBirth":"123123",
        "PassportSeries":"123123",
        "PassportNumber":"123123",
        "PassportIssued":"123123",
        "inn":"123123",
        "StudentLastname":"123123",
        "StudentFirstname":"123123",
        "StudentSurname":"123123",
        "StudentDateOfBirth":"123123",
        "StudentPassportSeries":"123123",
        "StudentPassportNumber":"123123",
        "StudentPassportIssued":"123123",
        "StudentINN":"123123",
        "date":"123123"},
    "tables": {
        "1":{"size":"100000",
                "context":["Коровы", "нюрка"]},
        "2":{"size":"50000",
                "context":["Собаки", "Шарик"]}
    },
    "meta_data": {
        "style":"",
        "alignment":"", #LEFT | CENTER | RIGHT
        "autofit":"", #1 | 0
    }
    
}
