from objectbox import Entity, Id, String

@Entity()
class Document:
    id = Id()
    text = String()
    embedding = String()  # Store embedding as a JSON string
