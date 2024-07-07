from faker import Faker

faker = Faker('pt_BR')

persona = {

    "nome": faker.name(),
    "cidade": faker.address()

}

print(persona)