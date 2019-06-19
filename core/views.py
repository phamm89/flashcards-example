from django.shortcuts import render, get_object_or_404
from core.models import Stack

# Create your views here.
def stack_list(request):
    stacks = Stack.objects.all()
    return render(request, 'core/stack_list.html', {"stacks": stacks})

def stack_detail(request, stack_pk):
    """
    View for /stacks/<stack_pk>
    Gets a stack and display all the cards in it.
    """
    stack = get_object_or_404(Stack, pk=stack_pk)
    stack = Stack.objects.get(pk=stack_pk)
    return render(request, 'core/stack_detail.html', {"stack": stack, "cards": stack.card_set.all(),})
