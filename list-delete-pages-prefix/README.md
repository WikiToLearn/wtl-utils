# Readme

## Description

This bot list or deletes all the pages with the indicated Prefix in the url.

## Config File

the config file has to be named `config.yaml` and has to be in `./` directory. It is 
gitignored, since it contains the user password and it strongly depends on the admin needs. There 
is a `config-template.yaml` that contains the scehme of the config file.

* `$lang` contains what domain the bot should upload the pages to, the complete list is [here](https://github.com/WikiToLearn/pywikibot/blob/master/wikitolearn_family.py)
* `$username` and `$password` contains the credentials that the bot should use to upload the pages the website,
* `$namespace` contains the namespace of the paegs that the admin wants to delete. It is `0` for "no specific template", it is "Course" for pages under the Course: template. for further info browse the [mediawiki template code reference](https://www.mediawiki.org/wiki/Manual:Namespace)
* `$prefix` : all this bot magic happens here. The admin should chose properly this parameter, since it governs this bot behaviuor. This bot wll delete every page whose link is of the form 
`$lang.$domain/$prefix*`.

`./` Contains an example, `config-example.yaml`,  to help understanding the config file. If this were `config.yaml`, it would remove all the pages whose link is 
"https://it.wikitolearn.vodka/Loreti-Teoria_degli_errori_e_Fondamenti_di_statistica/*"

## Run

`./delete-pages-prefix.sh` both build and run the docker, loading the config file dynamincally, so you have to build the container just once. 
Please note that the first time you run this it may take some time, since it has to pull the wikitolearn/pywikibot docker image

## Examples

If the file `config.yaml` is
```
pywikibot :
    lang: it
    user: user
    password: pass
namespace: Corso
prefix: Meccanica_quantistica
operation: list
```

then the bot lists the following pages (not all coming from the same course!!)

> Lang: it
> List of pages
> -------------
> Deleting page: Corso:Meccanica quantistica
> Deleting page: Corso:Meccanica quantistica/Calcolo della funzione d'onda
> Deleting page: Corso:Meccanica quantistica/Calcolo della funzione d'onda/La barriera di potenziale
> Deleting page: Corso:Meccanica quantistica/Calcolo della funzione d'onda/La buca di potenziale
> Deleting page: Corso:Meccanica quantistica/Calcolo della funzione d'onda/La doppia buca di potenziale
> Deleting page: Corso:Meccanica quantistica/Calcolo della funzione d'onda/Soluzione di problemi - Barriere
> Deleting page: Corso:Meccanica quantistica/Calcolo della funzione d'onda/Soluzione di problemi - Buche
> Deleting page: Corso:Meccanica quantistica/Formulario di Meccanica Quantistica
> Deleting page: Corso:Meccanica quantistica/Formulario di Meccanica Quantistica/Formulario di Meccanica Quantistica
> Deleting page: Corso:Meccanica quantistica/Il momento angolare
> Deleting page: Corso:Meccanica quantistica/Il momento angolare/Addizione di momenti angolari
> Deleting page: Corso:Meccanica quantistica/Il momento angolare/Autofunzioni di l^2 e l z: le armoniche sferiche
> Deleting page: Corso:Meccanica quantistica/Il momento angolare/Gli operatori gradino L + e L -
> Deleting page: Corso:Meccanica quantistica/Il momento angolare/Il momento angolare come generatore infinitesimo delle rotazioni
> Deleting page: Corso:Meccanica quantistica/Il momento angolare/Il momento angolare in meccanica quantistica
> Deleting page: Corso:Meccanica quantistica/Il momento angolare/Lo spin
> Deleting page: Corso:Meccanica quantistica/L'atomo di idrogeno
> Deleting page: Corso:Meccanica quantistica/L'atomo di idrogeno/Autofunzioni dell'atomo di idrogeno
> Deleting page: Corso:Meccanica quantistica/L'atomo di idrogeno/Equazione di Schrödinger per l'atomo di idrogeno
> Deleting page: Corso:Meccanica quantistica/L'atomo di idrogeno/Introduzione
> Deleting page: Corso:Meccanica quantistica/L'atomo di idrogeno/Note Aggiuntive
> Deleting page: Corso:Meccanica quantistica/L'atomo di idrogeno/Soluzione dell'equazione radiale
> Deleting page: Corso:Meccanica quantistica/L'atomo di idrogeno/Sulla stabilità degli autostati
> Deleting page: Corso:Meccanica quantistica/L'atomo di idrogeno/Sullo spin dell'elettrone
> Deleting page: Corso:Meccanica quantistica/La Meccanica Ondulatoria
> Deleting page: Corso:Meccanica quantistica/La Meccanica Ondulatoria/Calcolo della funzione della d'onda in alcuni casi di rilevanza pratica
> Deleting page: Corso:Meccanica quantistica/La Meccanica Ondulatoria/Il pacchetto d'onda
> Deleting page: Corso:Meccanica quantistica/La Meccanica Ondulatoria/L'equazione di Schrödinger
> Deleting page: Corso:Meccanica quantistica/La Meccanica Ondulatoria/L'ipotesi di de Broglie
> Deleting page: Corso:Meccanica quantistica/La Meccanica Ondulatoria/La funzione d'onda e sua interpretazione
> Deleting page: Corso:Meccanica quantistica/La Meccanica Ondulatoria/La particella libera
> Deleting page: Corso:Meccanica quantistica/La Meccanica Ondulatoria/Stati Stazionari
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/Costanti del moto e evoluzione temporale
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/Densità e corrente di probabilità
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/Evoluzione classica dei valori medi
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/Il principio di indeterminazione di Heisemberg
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/La funzione Delta di Dirac
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/La trasformata di Fourier. La funzione d'onda per l'impulso
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/Note riassuntive sulla struttura formale della teoria
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/Operatori Hermitiani e osservabili. L'apparato formale della teoria
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/Osservabili
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/Principi della meccanica quantistica
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/Proprietà dei commutatori
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/Separazione delle variabili e degenerazione. Numeri quantici.
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/Una dimostrazione generale della relazione di indeterminazione
> Deleting page: Corso:Meccanica quantistica/La struttura formale della meccanica quantistica/Valore atteso di una grandezza. La rappresentazione operatoriale
> Deleting page: Corso:Meccanica quantistica/Momento angolare orbitale
> Deleting page: Corso:Meccanica quantistica/Momento angolare orbitale/Armoniche sferiche
> Deleting page: Corso:Meccanica quantistica/Oscillatore armonico
> Deleting page: Corso:Meccanica quantistica/Oscillatore armonico/Metodo Analitico
> Deleting page: Corso:Meccanica quantistica/Oscillatore armonico/Metodo Operatoriale
> Deleting page: Corso:Meccanica quantistica/Oscillatore armonico/Oscillatore armonico
> Deleting page: Corso:Meccanica quantistica/Oscillatore armonico/Oscillatori armonici accoppiati
> Deleting page: Corso:Meccanica quantistica/Oscillatore armonico/Valori medi e stati coerenti
> Deleting page: Corso:Meccanica quantistica/Osservabili
> Deleting page: Corso:Meccanica quantistica/Principi della meccanica quantistica
> Deleting page: Corso:Meccanica quantistica/Rotatore Piano
> Deleting page: Corso:Meccanica quantistica/Rotatore Piano/Rotatore Piano
> Deleting page: Corso:Meccanica quantistica/Soluzioni di problemi - Barriere
> Deleting page: Corso:Meccanica quantistica/Soluzioni di problemi - Buche
> Deleting page: Corso:Meccanica quantistica/Teoria delle perturbazioni
> Deleting page: Corso:Meccanica quantistica/Teoria delle perturbazioni/Caso degenere
> Deleting page: Corso:Meccanica quantistica/Teoria delle perturbazioni/Caso non degenere
> Deleting page: Corso:Meccanica quantistica/Teoria delle perturbazioni/Introduzione
> Deleting page: Corso:Meccanica quantistica/Teoria delle perturbazioni/Metodo variazionale
> Deleting page: Corso:Meccanica quantistica/Teoria delle perturbazioni/Struttura Fine
> Deleting page: Corso:Meccanica quantistica/Teoria delle perturbazioni/Teoria delle perturbazioni dipendenti dal tempo
> Deleting page: Corso:Meccanica quantistica/Teoria delle perturbazioni/Teoria delle perturbazioni indipendenti dal tempo
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Atomo di idrogeno
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Atomo di idrogeno/Confronto della teoria con i dati sperimentali
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Atomo di idrogeno/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Atomo di idrogeno/La degenerazione nell'atomo di Idrogeno
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Atomo di idrogeno/Problema a due corpi
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Atomo di idrogeno/Ricerca di autofunzioni e autovalori radiali
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Atomo di idrogeno/Spettro dell'energia
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Atomo di idrogeno reale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Atomo di idrogeno reale/Accoppiamento spin-orbita
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Atomo di idrogeno reale/Energia cinetica relativistica
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Atomo di idrogeno reale/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Atomo di idrogeno reale/Somma delle perturbazioni
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Autovalori e autofunzioni della funzione d'onda
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Autovalori e autofunzioni della funzione d'onda/Autofunzioni dell'operatore momento
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Autovalori e autofunzioni della funzione d'onda/Degenerazione di stati
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Autovalori e autofunzioni della funzione d'onda/Operatore parità
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Autovalori e autofunzioni della funzione d'onda/Postulato di espansione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Composizione di momenti angolari
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Composizione di momenti angolari/Autofunzioni di J z e J^2
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Composizione di momenti angolari/Momento angolare totale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Composizione di momenti angolari/Somma di due momenti angolari generici
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Composizione di momenti angolari/Somma di due spin
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Dualismo onda particella
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Dualismo onda particella/Effetti della perturbazione dell'elettrone con una sorgente luminosa
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Dualismo onda particella/Funzione d'onda e probabilità
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Dualismo onda particella/Ipotesi di Born, Risposte di Einstein e Bohr
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Dualismo onda particella/Pacchetto d'onda
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Effetto Stark
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Effetto Stark/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Effetto Stark/Perturbazione dello stato fondamentale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Effetto Stark/Stato n=2
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Effetto Zeeman
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Effetto Zeeman/Effetto Zeeman anomalo
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Effetto Zeeman/Effetto Zeeman normale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Entanglement
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Entanglement/Paradosso EPR
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Entanglement/Paradosso del gatto di Schrodinger
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Entanglement/Stati Entangled
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Entanglement/Teletrasporto
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Equazione di Schrodinger indipendente dal tempo in 3 dimensioni
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Equazione di Schrodinger indipendente dal tempo in 3 dimensioni/Buca di potenziale tridimensionale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Equazione di Schrodinger indipendente dal tempo in 3 dimensioni/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Equazione di Schrodinger indipendente dal tempo in 3 dimensioni/Oscillatore armonico tridimensionale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Equazione di Schrodinger indipendente dal tempo in 3 dimensioni/Variabili separabili
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Equazione di Schrödinger
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Equazione di Schrödinger/Condizioni iniziali e phi(p)
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Equazione di Schrödinger/Derivazione dell'equazione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Equazione di Schrödinger/Equazione di continuità
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Equazione di Schrödinger/Postulati meccanica quantistica
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Evoluzione temporale del sistema
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Evoluzione temporale del sistema/Evoluzione temporale - visione di Heisenberg
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Evoluzione temporale del sistema/Teorema di Ehrenfest
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario argomenti Meccanica Quantistica
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario argomenti Meccanica Quantistica/Atomo di idrogeno
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario argomenti Meccanica Quantistica/Momento angolare
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario argomenti Meccanica Quantistica/Oscillatore Armonico
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario argomenti Meccanica Quantistica/Precessione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario argomenti Meccanica Quantistica/Teoria delle perturbazioni dipendenti dal tempo
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario argomenti Meccanica Quantistica/Teoria delle perturbazioni indipendenti dal tempo
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario argomenti Meccanica Quantistica/Teoria delle perturbazioni indipententi dal tempo
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico/Gamma di Eulero
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico/Integrale con gamma di Eulero
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico/Integrale gaussiano
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico/Laplaciano in coordinate sferiche
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico/Polinomi Di Hermite
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico/Real spherical harmonics
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico/Spherical Harmonics - spherical cartesian
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico/l = 0
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico/l = 1
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico/l = 2
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico/l = 3
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Formulario generico/l = 4
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Metodo Operatoriale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Metodo Operatoriale/Degenerazione e autofunzioni in comune
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Metodo Operatoriale/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Metodo Operatoriale/Operatori di proiezione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Momento Angolare
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Momento Angolare/Autovalori e autostati del momento angolare
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Momento Angolare/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Momento Angolare/Potenziale centrale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Momento Angolare/Soluzione dell'equazione agli autovalori
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Momento Angolare Orbitale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Momento Angolare Orbitale/Autovalori e autostati del momento angolare
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Momento Angolare Orbitale/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Momento Angolare Orbitale/Potenziale centrale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Momento Angolare Orbitale/Soluzione dell'equazione agli autovalori
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Operatori posizione e momento
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Operatori posizione e momento/Definizioni e valori d'aspettazione degli operatori posizione e momento
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Operatori posizione e momento/Operatori e osservabili fisiche
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Operatori posizione e momento/Proprietà degli operatori
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Operatori posizione e momento/Soluzione dell'equazione di Schrodinger in caso stazionario
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Operatori posizione e momento/Spazio dei momenti e spazio delle coordinate
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Oscillatore armonico quantistico
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Oscillatore armonico quantistico/Autostati dell'oscillatore armonico
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Oscillatore armonico quantistico/Cambio di variabili
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Oscillatore armonico quantistico/Energia di punto zero e principio di indeterminazione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Oscillatore armonico quantistico/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Oscillatore armonico quantistico/Metodo di Dirac
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Particella nella scatola
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Particella nella scatola/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Particella nella scatola/Osservazioni
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Particella nella scatola/Problema della normalizzazione delle onde piane
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Particelle In Campo Elettromagnetico
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Particelle In Campo Elettromagnetico/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Particelle In Campo Elettromagnetico/Meccanica Classica
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Particelle In Campo Elettromagnetico/Meccanica Quantistica
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Potenziali in una dimensione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Potenziali in una dimensione/Buca di potenziale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Potenziali in una dimensione/Gradino finito di potenziale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Potenziali in una dimensione/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Potenziali in una dimensione/Potenziale a doppia Delta
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Potenziali in una dimensione/Potenziale a singola Delta
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Potenziali in una dimensione/Potenziale con gradino
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Potenziali in una dimensione/Teorema di Degenerazione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Principio di indeterminazione di Heisenberg
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Principio di indeterminazione di Heisenberg/Dimostrazione del principio di Heisenberg
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Principio di indeterminazione di Heisenberg/Dimostrazione generale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Principio di indeterminazione di Heisenberg/Enunciazione del principio
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Principio di indeterminazione di Heisenberg/Esempi di applicazione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Problemi della fisica classica
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Problemi della fisica classica/Effetto Compton
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Problemi della fisica classica/Effetto Fotoelettrico
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Problemi della fisica classica/Esperimento della doppia fenditura
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Problemi della fisica classica/Esperimento di Nichols Hull
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Problemi della fisica classica/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Problemi della fisica classica/Ipotesi di De Broglie
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Problemi della fisica classica/Problema del Corpo Nero
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Problemi della fisica classica/Stabilità dell'atomo
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Prodotto Tensoriale
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Prodotto Tensoriale/Definizione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Prodotto Tensoriale/Prodotto Tensoriale di Operatori
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Prodotto Tensoriale/Uso del prodotto tensoriale in Meccanica Quantistica
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Spin
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Spin/Analogie con il momento angolare
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Spin/Autovalori e Autostati
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Spin/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Spin/Matrici di Pauli
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Spin/Momento magnetico intrinseco
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Spin/Valore d'aspettazione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Teoria delle perturbazioni
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Teoria delle perturbazioni/Approssimazione al primo ordine
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Teoria delle perturbazioni/Approssimazioni al secondo ordine
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Teoria delle perturbazioni/Degenerazione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Teoria delle perturbazioni/Introduzione
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Teoria delle perturbazioni/Teoria delle perturbazioni al secondo ordine degenere
> Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Teoria delle perturbazioni dipendenti dal tempo
Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Teoria delle perturbazioni dipendenti dal tempo/Introduzione
Deleting page: Corso:Meccanica quantistica (Gasiorowicz)/Teoria delle perturbazioni dipendenti dal tempo/Perturbazioni armoniche
