from flask.cli import FlaskGroup

from project import app, db, SuperHeroes, Chronicles


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(SuperHeroes(
        superhero_name="Spiderman"
        , superhero_power=8
        , is_villain=False
    ))
    db.session.add(SuperHeroes(
        superhero_name="Iron Man"
        , superhero_power=9
        , is_villain=False
    ))
    db.session.add(SuperHeroes(
        superhero_name="Mysterio"
        , superhero_power=7
        , is_villain=True
    ))
    db.session.add(Chronicles(
        hero_id=2
        , year=2019
        , text='died'
    ))
    db.session.add(Chronicles(
        hero_id=3
        , year=2019
        , text='lost to Spiderman'
    ))
    db.session.add(Chronicles(
        hero_id=1
        , year=2021
        , text='opened multiverse'
    ))
    db.session.commit()


if __name__ == "__main__":
    cli()