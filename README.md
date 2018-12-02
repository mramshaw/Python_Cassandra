# Cassandra with Python

![Cassandra](images/Cassandra.png)

Cassanda is a [NoSQL](http://en.wikipedia.org/wiki/NoSQL) database that originated at Facebook.

Cassandra is optimized for fast writes and fast reads over very large volumes of data.

In contrast with traditional databases that journal database changes and then write them to disk,
Cassandra journals database changes and then writes them to a ___write-back cache___ (also known
as a ___write-behind cache___) - and only writes the cache to disk once the cache fills.

```
    Journal --> Cache --> Disk 
```

The Cassandra terms for these are the __commit log__, __Memtables__ and __SS Tables__ [which
stands for ___Sorted String Tables___ (these are immutable).] The database write is successful
and returns once the data is written to the __Memtable__. How this data gets written to disk
and propogated then depends on the ___replication policy___ (we will use simple replication).

By design, there is no single point of failure.

In terms of the [CAP or Brewer's theorem](http://en.wikipedia.org/wiki/Cap_theorem), Cassandra is an ___eventually-consistent___
database. This means that replicas of a row may have different versions of the data - but only for brief periods. The replicas
will __eventually__ be synchronized and become consistent (hence the term).

![CAP and Cassandra](images/CAP_Cassandra.png)

## Motivation

Familiarization with `Cassandra` and `cqsql` with Python, using the [Datastax driver](http://datastax.github.io/python-driver/index.html).

This exercise follows on from my [Replicated Cassandra Database](http://github.com/mramshaw/Kubernetes/tree/master/Replicated%20Cassandra%20Database) exercise.

## Prerequisites

* Python installed

* `pip` installed

## Cassandra driver

#### Installation

Install Cassandra driver as follows:

    $ pip install --user cassandra-driver

Or else:

    $ pip install --user -r requirements.txt

#### Verification

Verify installation as follows:

```bash
$ python -c 'import cassandra; print cassandra.__version__'
3.16.0
$
```

Or:

```bash
$ pip list --format=freeze | grep cassandra-driver
cassandra-driver==3.16.0
$
```

#### Compression

Optionally, install `lz4` (gets installed with `cassandra-driver` if using `requirements.txt`):

    $ pip install --user lz4

Verify installation as follows:

```bash
$ python -c 'import lz4; print lz4.__version__'
2.1.2
$
```

Or:

```bash
$ pip list --format=freeze | grep lz4
2.1.2
$
```

#### Metrics

Optionally, install `scales` (gets installed with `cassandra-driver` if using `requirements.txt`):

    $ pip install --user scales

The driver has built-in support for capturing Cluster.metrics about the queries run. The scales library is required to support this.

#### Performance

Optionally, install `libev` for better performance.

Verify the presence (or - as below - absence) of `libev` as follows:

```bash
$ python -c 'from cassandra.io.libevreactor import LibevConnection'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/owner/.local/lib/python2.7/site-packages/cassandra/io/libevreactor.py", line 33, in <module>
    "The C extension needed to use libev was not found.  This "
ImportError: The C extension needed to use libev was not found.  This probably means that you didn't have the required build dependencies when installing the driver.  See http://datastax.github.io/python-driver/installation.html#c-extensions for instructions on installing build dependencies and building the C extension.
$
```

Installation instructions are here:

    http://datastax.github.io/python-driver/installation.html#libev-support

[We will not be installing `libev`.]

## Versions

* python __2.7.12__
* pip __18.1__
* cassandra-driver __3.16.0__
* lz4 __2.1.2__
* scales __1.0.9__

## To Do

- [ ] More testing

## Credits

There are many fine resources for learning Cassandra. The place to start is:

    http://datastax.github.io/python-driver/getting_started.html

[Well worth careful study for the sections on
 [type conversion](http://datastax.github.io/python-driver/getting_started.html#type-conversions),
 [consistency level](http://datastax.github.io/python-driver/getting_started.html#setting-a-consistency-level)
and
 [prepared statements](http://datastax.github.io/python-driver/getting_started.html#id2).
]

Also:

    http://datastax.github.io/python-driver/installation.html
