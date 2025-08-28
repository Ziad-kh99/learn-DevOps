namespace TodoApi.Data;

using Microsoft.EntityFrameworkCore;
using TodoApi.Models;

class TodoDb : DbContext
{
    public TodoDb(DbContextOptions<TodoDb> options) : base(options)
    { }

    public DbSet<Todo> Todos => Set<Todo>();
}