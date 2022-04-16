create table pokemon (
 	'id' integer primary key,
	'name' text not null,
	'attack' integer not null,
	'defense' integer not null,
	'hp' integer not null
);
 
create table pokemon_type (
 	'id' integer not null,
 	'type_1' text not null,
 	'type_2' text default null,
 	foreign key ('id') references 'pokemon' ('id')
 );
 
create table effectiveness (
	'attack_type' text not null, 
	'defense_type' text not null, 
	'effect' float not null,
	primary key ('attack_type', 'defense_type')
);

create table evolves (
	'id' integer not null,
	'from_id' integer,
	'to_id' integer,
	foreign key ('id') references 'pokemon' ('id'),
	foreign key ('from_id') references 'pokemon' ('id'),
	foreign key ('to_id') references 'pokemon' ('id')
);

create table trainer (
	'id' integer primary key,
	'name' integer not null
);

create table trainer_pokemon (
	'trainer_id' integer not null,
	'pokemon_id' integer not null,
	foreign key ('trainer_id') references 'trainer' ('id'),
	foreign key ('pokemon_id') references 'pokemon' ('id')
);
