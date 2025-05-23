from argparse import ArgumentParser,Action

class DriverAction(Action):
    def __call__(self,parser,namespace,values,option_string=None):
        driver,destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description="""
    Back up PostgreSQL databases locally or to AWS S3
    """)

    parser.add_argument("url",help="Url of the database to backup")
    parser.add_argument("--driver",
                        help="how & where to store backup",
                        nargs=2, # 2 arguments required
                        action=DriverAction, # Custom action
                        required=True
                        )
    return parser


def main():
    import boto3
    from pgbackup import pgdump,storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        print(f"Backing up database to {args.destination} in S3")
        storage.s3(client,dump.stdout,args.destination,args.url)
    else:
        outfile = open(args.destination,'wb')
        print(f"Backing up database to {args.destination}")
        storage.local(dump.stdout,outfile)