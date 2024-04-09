


class IdGeneratorOptions:


    def __init__(self, worker_id=0, worker_id_bit_length=6, seq_bit_length=6):

        self.method = 1

        self.base_time = 1288834974657

        self.worker_id = worker_id

        self.worker_id_bit_length = worker_id_bit_length

        self.seq_bit_length = seq_bit_length

        self.max_seq_number = 0

        self.min_seq_number = 5

        self.top_over_cost_count = 2000
