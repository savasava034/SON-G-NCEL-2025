#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARISTO Module: Priority Management
Task and query priority management system
"""

from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum
import heapq


class Priority(Enum):
    """Priority levels"""
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4


class PriorityModule:
    """Priority management module"""
    
    def __init__(self):
        """Initialize priority module"""
        self.queue = []
        self.tasks = {}
        self.counter = 0
    
    def add_task(self,
                 task_id: str,
                 description: str,
                 priority: Priority = Priority.MEDIUM,
                 metadata: Optional[Dict] = None) -> bool:
        """
        Add a task to the priority queue
        
        Args:
            task_id: Unique task identifier
            description: Task description
            priority: Task priority level
            metadata: Additional task metadata
        
        Returns:
            bool: Success status
        """
        task = {
            'id': task_id,
            'description': description,
            'priority': priority,
            'created_at': datetime.now().isoformat(),
            'metadata': metadata or {},
            'status': 'pending'
        }
        
        # Use heap for priority queue
        # (priority_value, counter, task_id) to maintain order
        heapq.heappush(self.queue, (priority.value, self.counter, task_id))
        self.tasks[task_id] = task
        self.counter += 1
        
        return True
    
    def get_next_task(self) -> Optional[Dict]:
        """
        Get the next highest priority task
        
        Returns:
            dict: Task data or None if queue is empty
        """
        if not self.queue:
            return None
        
        _, _, task_id = heapq.heappop(self.queue)
        task = self.tasks.get(task_id)
        
        if task:
            task['status'] = 'in_progress'
        
        return task
    
    def complete_task(self, task_id: str) -> bool:
        """
        Mark a task as completed
        
        Args:
            task_id: Task identifier
        
        Returns:
            bool: Success status
        """
        if task_id in self.tasks:
            self.tasks[task_id]['status'] = 'completed'
            self.tasks[task_id]['completed_at'] = datetime.now().isoformat()
            return True
        return False
    
    def cancel_task(self, task_id: str) -> bool:
        """
        Cancel a task
        
        Args:
            task_id: Task identifier
        
        Returns:
            bool: Success status
        """
        if task_id in self.tasks:
            self.tasks[task_id]['status'] = 'cancelled'
            self.tasks[task_id]['cancelled_at'] = datetime.now().isoformat()
            return True
        return False
    
    def update_priority(self, task_id: str, new_priority: Priority) -> bool:
        """
        Update task priority
        
        Args:
            task_id: Task identifier
            new_priority: New priority level
        
        Returns:
            bool: Success status
        """
        if task_id not in self.tasks:
            return False
        
        # Remove old entry and add new one
        # (This is a simplified approach; in production, use a more efficient method)
        self.queue = [(p, c, tid) for p, c, tid in self.queue if tid != task_id]
        heapq.heapify(self.queue)
        
        self.tasks[task_id]['priority'] = new_priority
        heapq.heappush(self.queue, (new_priority.value, self.counter, task_id))
        self.counter += 1
        
        return True
    
    def get_task(self, task_id: str) -> Optional[Dict]:
        """
        Get task by ID
        
        Args:
            task_id: Task identifier
        
        Returns:
            dict: Task data or None
        """
        return self.tasks.get(task_id)
    
    def list_tasks(self, 
                   status: Optional[str] = None,
                   priority: Optional[Priority] = None) -> List[Dict]:
        """
        List tasks with optional filters
        
        Args:
            status: Filter by status
            priority: Filter by priority
        
        Returns:
            list: List of tasks
        """
        tasks = list(self.tasks.values())
        
        if status:
            tasks = [t for t in tasks if t['status'] == status]
        
        if priority:
            tasks = [t for t in tasks if t['priority'] == priority]
        
        return sorted(tasks, key=lambda x: x['created_at'], reverse=True)
    
    def get_queue_status(self) -> Dict:
        """
        Get queue status summary
        
        Returns:
            dict: Queue statistics
        """
        pending = [t for t in self.tasks.values() if t['status'] == 'pending']
        in_progress = [t for t in self.tasks.values() if t['status'] == 'in_progress']
        completed = [t for t in self.tasks.values() if t['status'] == 'completed']
        
        return {
            'total': len(self.tasks),
            'pending': len(pending),
            'in_progress': len(in_progress),
            'completed': len(completed),
            'queue_length': len(self.queue)
        }
    
    def clear_completed(self) -> int:
        """
        Remove completed tasks
        
        Returns:
            int: Number of tasks cleared
        """
        completed_ids = [
            tid for tid, task in self.tasks.items()
            if task['status'] == 'completed'
        ]
        
        for tid in completed_ids:
            del self.tasks[tid]
        
        return len(completed_ids)


# Module instance
priority_module = PriorityModule()


def add_task(task_id: str, description: str, priority: str = 'medium') -> bool:
    """
    Add a prioritized task
    
    Args:
        task_id: Task identifier
        description: Task description
        priority: Priority level ('critical', 'high', 'medium', 'low')
    
    Returns:
        bool: Success status
    """
    priority_map = {
        'critical': Priority.CRITICAL,
        'high': Priority.HIGH,
        'medium': Priority.MEDIUM,
        'low': Priority.LOW
    }
    
    priority_enum = priority_map.get(priority.lower(), Priority.MEDIUM)
    return priority_module.add_task(task_id, description, priority_enum)


def get_next_task() -> Optional[Dict]:
    """
    Get next task from priority queue
    
    Returns:
        dict: Next task or None
    """
    return priority_module.get_next_task()
