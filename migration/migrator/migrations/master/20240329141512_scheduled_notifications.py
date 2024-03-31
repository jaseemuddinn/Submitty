"""Migration for the Submitty master database."""


def up(config, database):
    """
    Run up migration.

    :param config: Object holding configuration details about Submitty
    :type config: migrator.config.Config
    :param database: Object for interacting with given database for environment
    :type database: migrator.db.Database
    """
    database.execute(
        """
            CREATE TABLE scheduled_notifications (
                id SERIAL PRIMARY KEY,
                reference_id character varying(255) NOT NULL,
                type character varying(255) NOT NULL,
                term character varying NOT NULL,
                course character varying NOT NULL,
                date timestamp(6) with time zone NOT NULL,
                notification_state boolean DEFAULT false NOT NULL
            );
        """
    )


def down(config, database):
    """
    Run down migration (rollback).

    :param config: Object holding configuration details about Submitty
    :type config: migrator.config.Config
    :param database: Object for interacting with given database for environment
    :type database: migrator.db.Database
    """
    database.execute(
        """
            DROP TABLE scheduled_notifications;
        """
    )
