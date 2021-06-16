from core.pyba_logic import PybaLogic

class FilmLogic(PybaLogic):
    def _init_(self):
        super()._init_()

    def getFilmById(self, id):
        database = self.createDatabaseObj()
        sql = f"select * from film where film_id={id};"
        result = database.executeQuery(sql)
        return result

    def insertFilm(self, film):
        database = self.createDatabaseObj()
        sql = (
            f"INSERT INTO `sakila`.`film`"
            + f"(`film_id`,`title`,`description`,`release_year`, `language_id`,`original_language_id`,`rental_duration`,`rental_rate`,`length`,`replacement_cost`,`rating`,`special_features`,`last_update`) "
            + f"VALUES(0, '{film['title']}', '{film['description']}', '{film['release_year']}', {film['language_id']}, {film['original_language_id']}, {film['rental_duration']}, {film['rental_rate']}, {film['length']}, {film['replacement_cost']}, '{film['rating']}', '{film['special_features']}', '{film['last_update']}'"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateFilm(self, id, film):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE `sakila`.`film` "
            + f"SET `title` = '{film['title']}', `description` = '{film['description']}', `release_year` = '{film['release_year']}', `language_id` = {film['language_id']}, `original_language_id` = {film['original_language_id']}, `rental_duration` = {film['rental_duration']}, `rental_rate` = {film['rental_rate']}, `length` = {film['length']}, `replacement_cost` = {film['replacement_cost']}, `rating` = '{film['rating']}', `special_features` = '{film['special_features']}',`last_update` = '{film['last_update']}'"
            + f"WHERE `film_id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteFilm(self, id):
        database = self.createDatabaseObj()
        sql = f"delete from film where id={id};"
        rows = database.executeNonQueryRows(sql)
        return rows