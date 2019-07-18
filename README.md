# Projeto de estudo de GraphQL

## Variaveis de ambiente 

    DATABASE_URI=mongodb://localhost:27017/

## Rota - /graphql

### Mutation 

#### Create Person

    mutation myMutations{
      createPerson(personData: {name: "Gustavo", age: 22, nickname: "saboia", bestFriend: "fulanin"}){
        person{
          name
          nickname
          age
          id
        }
      }
    }
    
### Queries

#### Persons 

    {
      persons{
        id
        name
        nickname
        age
        bestFriend
      }
    }
    
#### Person

    {
      person{
        id
        name
        nickname
        age
        bestFriend
      }
    }