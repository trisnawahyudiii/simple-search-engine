DROP TABLE IF EXISTS documents;
DROP TABLE IF EXISTS term_frequency;

-- Create 'documents' table to store documents with text, creation date, and deletion date.
CREATE TABLE documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
);

-- Create 'term_frequency' table to store TF values associated with documents.
CREATE TABLE term_frequency (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    term TEXT NOT NULL,
    tf_value DOUBLE PRECISION NOT NULL,
    document_id INTEGER,
    FOREIGN KEY (document_id) REFERENCES documents(id)
);
