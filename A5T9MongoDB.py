""" 
Important notes wrt Task 9: 

Unlike MongoDB, SQLite (or SQL-based DBMS in general for that matter) does not have a native way to do text-based similarity searches. Fortunately "FTS5 is an SQLite virtual table module that provides full-text search functionality to database applications." Hence, once a virtual table is built using the reviews information (refer to this link for more information) if the user provides a set of keywords as the query terms all one need to do is to issue a query using FTS5's boolean operators (refer to this link for more information). The appendix below has some sample usage of SQLite's FTS5 module.
The ordering of the returned listings may not be identical, and that's OK. This is beyond the scope of the course, but SQLite and MongoDB may use different ways to compare documents, e.s., SQLite's TFS5 uses BM25, and while I couldn't find a reference ("certified" by MongoDB) for how MongoDB does it this document discusses it works well though.
"""

""" Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".  """