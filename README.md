# StarSchemaBenchmark

This is a simple copy of the table generation code from O'Neil et al.'s Star Schema Benchmark as
described in the following paper:

Patrick O'Neil, Elizabeth (Betty) O'Neil and Xuedong Chen. "The Star Schema Benchmark," Online Publication of Database Generation program., January 2007.
http://www.cs.umb.edu/~poneil/StarSchemaB.pdf

Changes with this copy : 

        - Generating csv files instead of csv.
        - Changing the SEPARATOR to comme instead of |.

# Usage

        make
        
        (customer.csv)
        dbgen -s 1 -T c
        
        (part.csv)
        dbgen -s 1 -T p
        
        (supplier.csv)
        dbgen -s 1 -T s
        
        (date.csv)
        dbgen -s 1 -T d
        
        (fact table lineorder.csv)
        dbgen -s 1 -T l
        
        (for all SSBM tables)
        dbgen -s 1 -T a


	python dbgen.py
	this will generate ssbRaw.csv:
		combining part.csv and customer.csv  with the lineorder.csv
These commands should generate the following files: customer.csv  date.csv      lineorder.csv part.csv      supplier.csv

You can easily generate larger files by modifying the scale parameter (-s).


To generate the refresh (insert/delete) data set: 

        dbgen -s 1 -r 5 -U 4

where "-r 5" specifies refreshin fact n/10000 "-U 4" specifies 4 segments for deletes and inserts. This will create the files create delete.[1-4] and lineorder.csv.u[1-4] with refreshing fact 0.05%.


# Suitability

This is strictly for research purposes. 
