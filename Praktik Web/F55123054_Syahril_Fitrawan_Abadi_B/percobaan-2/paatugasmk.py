class Node:
    def __init__(self, level, path, bound):
        self.level = level    
        self.path = path       
        self.bound = bound     

def branch_and_bound_job_scheduling(jobs):
    # Hitung nilai batas awal
    initial_bound = calculate_initial_bound(jobs)
    root = Node(0, [], initial_bound)
    best_cost = float('inf')
    best_path = []

    # Antrian prioritas untuk simpul yang belum diproses
    queue = PriorityQueue()
    queue.put((root.bound, root))

    while not queue.empty():
        _, node = queue.get()

        if node.bound < best_cost:
            for i in range(len(jobs)):
                if i not in node.path:
                    new_path = node.path + [i]
                    new_bound = calculate_bound(new_path, jobs)

                    # Jika sudah mencapai akhir atau solusi yang lebih baik ditemukan
                    if len(new_path) == len(jobs):
                        total_cost = calculate_total_cost(new_path, jobs)
                        if total_cost < best_cost:
                            best_cost = total_cost
                            best_path = new_path
                    elif new_bound < best_cost:
                        new_node = Node(node.level + 1, new_path, new_bound)
                        queue.put((new_node.bound, new_node))

    return best_path, best_cost
