You just started working for a company that sells products for a couple of countries in the world.

The Data Engineering team set up a process where you will receive a file into an s3 bucket on a daily basis.
The file will be under the following folder:

```data/YYYY-MM-DD/platform_transactions.csv```

For example, in there you should have:

```data/2023-07-01/platform_transactions.csv```

```data/2023-07-02/platform_transactions.csv```

```data/2023-07-03/platform_transactions.csv```

```data/2023-07-04/platform_transactions.csv```

```etc...```

This repository should contain a framework to:

- Grab the data from an s3 bucket
- Clean/transform the data
- Ingest into a Data Warehouse
- Create 2 reports
  - Total value of transactions and send to the Finance Team
  - Total number of transactions and sent to the Marketing Team

Details:

- Our data warehouse details are set up in the config folder
- The data warehouse only contains 1 database, 1 schema, and 1 table inside it. All are defined inside the config folder too.
- At the moment, only 2 reports are created, one for the Finance Team and another one for the Marketing Team

You arrive on your first day at the job and see this repository. In the current state, the scripts work, it can manage all tasks required.
But there are new clients and products that will be added to the company soon, and more teams will request new reports, what would you do?

Would you change the current state of the repository or not? If you decide to do some changes, fork this repo and share with us!
