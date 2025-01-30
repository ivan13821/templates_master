
import requests
import json

def test_add_file():
    file_name = "Приказ_о_заявлении_для_налоговой.docx"
    file = open(f"templates/{file_name}", "rb")



    test_response = requests.post(
    "http://127.0.0.1:8000/upload", 
    data={
        'filename': file_name,
        "type" : "multipart/form-data"
        }, 
        files = { "file" : file  } 
    ) 
    file.close()
    test_response.text

    print(test_response.text)






def generate_pdf():

    context = json.dumps({
        "file_name": "Приказ_о_заявлении_для_налоговой",
        "context":
        {
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
        },
        "signature":""
    })

    data = requests.post(url="http://127.0.0.1:8000/", data=context)

    with open(f"Приказ_о_заявлении_для_налоговой.pdf", 'wb') as f:
        f.write(data.content)
    


generate_pdf()
#test_add_file()