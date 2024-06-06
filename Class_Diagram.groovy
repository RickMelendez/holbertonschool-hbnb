ClassDiagram
    class User {
        +String id
        +String email
        +String first_name
        +String last_name
        +String password
        +Date created_at
        +Date updated_at
        +login()
        +logout()
    }

    class Place {
        +String id
        +String name
        +String description
        +String address
        +int price
        +Date created_at
        +Date updated_at
        +book()
        +cancelBooking()
    }

    class Review {
        +String id
        +String text
        +int rating
        +Date created_at
        +Date updated_at
        +String user_id
        +String place_id
        +submit()
        +edit()
        +delete()
    }

    class Amenity {
        +String id
        +String name
    }

    class Country {
        +String id
        +String name
        +String code
    }

    class City {
        +String id
        +String name
        +String country_id
    }

    %% Relationships
    User "1" --> "0..*" Place : owns
    Place "0..*" --> "0..*" Review : has
    Place "0..*" --> "0..*" Amenity : includes
    City "1" --> "0..*" Place : located_in
    Country "1" --> "0..*" City : contains
    User "1" --> "0..*" Review : writes
    Place "0..*" --> "1" User : booked_by
