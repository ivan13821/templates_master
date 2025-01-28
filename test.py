from worker.main import MyFile


context = {
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
    "date":"123123"
    }

MyFile.generete_txt(context=context, file_name="Приказ_о_заявлении_для_налоговой")