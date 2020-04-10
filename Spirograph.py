class TriangleSpirograph:
    def __init__(self, p1, p2, p3, n_points, n_mult):
        """Creates a triangle spirograph at vertices p1, p2, and p3 with n_points evenly 
        spaced over the line segments. Lines are drawn between a point x and point x * n_mult % n_points at each update"""
        
        self.frame_count = 0
        
        self.n, self.x = n_points, n_mult
        self.p1, self.p2, self.p3 = p1, p2, p3
        
        self.ps = self.even_partition(self.n, self.p1, self.p2, self.p3)
        
        self.PAUSED = False
        self.TO_MOVE = False
   
    def next_setup(self):
        self.x += 1
        self.frame_count = 0
   
    def draw_triangle(self):
         triangle(self.p1.x, self.p1.y,
                  self.p2.x, self.p2.y,
                  self.p3.x, self.p3.y)    
    
    def draw_next_line(self):
        """Draws line from point current point to point * n_mult % n_points"""
        
        if self.PAUSED:
            return 
        
        x1, y1 = self.ps[self.frame_count]
        x2, y2 = self.ps[self.frame_count * self.x % self.n]
        
        line(x1, y1, x2, y2)
        
        self.frame_count += 1
    
    @staticmethod
    def even_partition(n, p1, p2, p3):
        """Partitions into n points of spirograph and returns a list with each index 
           corresponding to a numbered point"""
        
        points = [0] * n
    
        d1 = dist(p1.x, p1.y, p2.x, p2.y)
        d2 = dist(p2.x, p2.y, p3.x, p3.y)
        d3 = dist(p3.x, p3.y, p1.x, p1.y)
        
        ps = [p1, p2, p3]
        ds = [d1, d2, d3]
        
        n_ps = len(ps)
        total = sum(ds)
        
        j = 1
        dt = total / float(n)
        prev, current = 0, d1
        curr_p, next_p = p1, p2
        for i in xrange(1, n+1):
            if i * dt > current:
                prev = current
                current += ds[j]
                
                j += 1
                curr_p = next_p
                next_p = ps[j % n_ps]
            
            p = (i*dt-prev) / (current-prev)
            points[i-1] = PVector.lerp(curr_p, next_p, p)
            points[i-1] = (points[i-1].x, points[i-1].y)
        
        return points
