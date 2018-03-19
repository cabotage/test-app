default:
	@tar -czf cabotage.tgz --exclude './cabotage.tgz' .

clean:
	rm cabotage.tgz
