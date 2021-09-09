"""Apache Flink"""
"""Apache Flink
WHAT: open source stream processing framework and distributed processing engine over unbounded and bounded data streams.

    Low latency
    
    High throughput
    
    Stateful computations
        Batch processing: static data
        Data stream processing: live data
        Event driven applications
        
    Distributed: scalable
    
WHY:

    Streaming ETL
        data pipelines continuously move data >< traditional periodic ETL
        Ingestion with low latency
        No artificial data boundaries
        
    Data analytics - Stream analytics continuously processes data:
        Data changes faster than queries
        Provide FAST and CORRECT results >< traditional Lambda architecture: batch processor for correct data and\
            streaming processor for false data
            
    Event-driven application
        Locally maintained state >< state remotely stored in database
        Guaranteed consistency via periodic state checkpoints
        Highly scalable => microservice structure where everything is stored in flink and each streaming job works \
            on a specific problem
            
    APIs:
        Stream & batch processing: datastream API (streams, windows)
        Analytics: stream sql, table API (dynamic tables)
        Stateful event-driven applications: process function (events, state, time)
WHEN: 

    Initial release - May 2011; 9 years ago
    Stable release - 7 December 2020; 41 days ago
    
WHO: apache software foundation

WHERE: America

HOW: core building blocks

    Event streams: real time and hindsight data
        Source => transform => window(state read.write) => sink
        Scalable embedded state => access at memory speed and scales with parallel operators
        
    State: backup, restore data => guarantee
        
    Event (time): consistency with out-of-order data and late data
        Event time: usres’ time, exactly in real-world time order => however may cause high latency
        Broker time: events delivered to message queue => time stamps
        Ingestion: go into flink => flink assigns time stamps when events arrive in system
        Window processing time: go into windows processor => time of machine processing event in window operator \
            => ultra low latency
            
    Snapshots: forking/versioning/time-travel
"""
